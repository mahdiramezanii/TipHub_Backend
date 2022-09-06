from Tutorial_app.models import Category
from Acount_app.models import Techer
from django.shortcuts import redirect

def categorydata(request):

    context=Category.objects.all()

    return {
        "category":context
    }

def check_activ_teacher(request):

    if request.user.is_authenticated:
        user=request.user
        teacher=Techer.objects.filter(user=user,is_active=True).exists()
        if teacher:

            return {"is_teacher":True}

        return {"is_teacher":False}
    return {"is_teacher": False}