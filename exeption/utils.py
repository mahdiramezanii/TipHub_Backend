from . import jalali
from django.utils import timezone

def jalali_convert(time):


    jmunth=[
        "فروردین",
        "اردیبهشن",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    ]

    time=timezone.localtime(time)

    time_to_str="{},{},{}".format(time.year,time.month,time.day)
    time_to_tuple=jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list=list(time_to_tuple)

    for index,month in enumerate(jmunth):
        if time_to_list[1]==index+1:
            time_to_list[1]=month
            break

    output="{}/{}/{},ساعت {}:{}".format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0],
        time.hour,
        time.minute,
    )

    return output