import requests
from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, View, FormView, CreateView, DetailView
from .forms import LoginForm, EditUserForm
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from Acount_app.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from Acount_app.models import User, Techer
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .mixin import RedirectLogin, CheckLogin
from Acount_app.forms import CreateTeacherForm
from django.conf import settings


class ProfileUser(CheckLogin, TemplateView):
    template_name = "Acount_app/user_panel.html"


class ProfileEdit(View):

    def post(self, request):
        form = EditUserForm(
            request.POST,
            request.FILES,
            instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("Acount_app:profile")

    def get(self, request):
        form = EditUserForm(instance=request.user)
        return render(request, "Acount_app/edit_user_panel.html", {"form": form})


class PasswordResetRequest(RedirectLogin, View):

    def post(self, request):
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "Acount_app/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email,settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")

    def get(self, request):
        password_reset_form = PasswordResetForm()
        return render(request=request, template_name="Acount_app/password/password_reset.html",
                      context={"password_reset_form": password_reset_form})


"""def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "Acount_app/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")

                
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="Acount_app/password/password_reset.html",
                  context={"password_reset_form": password_reset_form})"""


class LoginView(RedirectLogin, View):
    template_name = "Acount_app/login.html"

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get("username"))
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect("/")

        return render(request, "Acount_app/login.html", {"form": form})

    def get(self, request):
        form = LoginForm()

        return render(request, "Acount_app/login.html", {"form": form})


"""class RegisterView(FormView):
    template_name = "Acount_app/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("Home:Home")

    def form_valid(self, form):
        form = form.cleaned_data
        username = form.get("username")
        email = form.get("email")
        password1 = form.get("password1")
        user = User.objects.create(username=username, email=email, password=password1)
        user.set_password(password1)
        login(self.request, user)
        return super().form_valid(form)"""


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect("Home:Home")


class RegisterView(RedirectLogin, CreateView):
    template_name = "Acount_app/register.html"
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your blog account.'
        message = render_to_string('Acount_app/acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message,settings.DEFAULT_FROM_EMAIL, to=[to_email]
        )
        email.send()
        return HttpResponse('لینک فعال سازی برای شما ارسال شد')


def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect("Acount_app:Login")

    else:
        return HttpResponse('Activation link is invalid!')


class ProfileTeacher(DetailView):
    template_name = "Acount_app/profile.html"
    model = Techer

    def get_context_data(self, **kwargs):
        context = super(ProfileTeacher, self).get_context_data(**kwargs)
        user = self.request.user
        teacher = Techer.objects.get(id=self.object.pk)

        if user in teacher.followers.all():
            context["follow"] = True
        else:
            context["follow"] = False
        return context

    def post(self, request, slug,pk):
        user=request.user
        teacher = Techer.objects.get(pk=pk)


        if user in teacher.followers.all():
            teacher.followers.remove(request.user)

        else:

            teacher.followers.add(request.user)

        return redirect(reverse_lazy("Acount_app:profile_teacher",kwargs={"pk":pk,"slug":slug}))


class CreateTeacher(View):

    def post(self,request):
        form=CreateTeacherForm(request.POST,request.FILES)

        if form.is_valid():

            cd = form.cleaned_data
            about_me = cd.get("about_me")
            resume = cd.get("resume")

            if not Techer.objects.filter(user=request.user).exists():
                t=Techer.objects.create(user=request.user)
                t.resume=resume
                t.about_me=about_me
                t.save()
                return redirect("Home:Home")
            return render(request,"Acount_app/create_teacher.html",{"form":form})


    def get(self, request):
        form=CreateTeacherForm()

        return render(request,"Acount_app/create_teacher.html",{"form":form})