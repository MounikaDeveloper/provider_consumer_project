from django.shortcuts import render

# Create your views here.
from customerapp.models import CustomerDetails1
from django.core.mail import send_mail
from OnlineSale import settings as se
import random
def clogin(request):
    cno=request.POST.get("cno")
    pwd=request.POST.get("pwd")
    c=CustomerDetails1.objects.filter(contactno=cno,password=pwd)
    if c:
        return render(request,"customer_template/customerapplication.html",{"msg":"Login Successful"})
    else:
        return render(request, "customer_template/customerapplication.html", {"msg": "Incorrect Details"})


def creg(request):
    name=request.POST.get("name")
    cno=request.POST.get("cno")
    address=request.POST.get("address")
    email=request.POST.get("email")
    pwd=request.POST.get("pwd")
    otp1= random.randint(1000, 9999)
    send_mail("OTP","OTP for login:"+str(otp1),se.EMAIL_HOST_USER,[email])
    CustomerDetails1(name=name, contactno=cno, address=address,status="pending", email=email, password=pwd,otp=otp1).save()
    return render(request,"customer_template/c_emailotp.html")


def otp(request):
    email = request.POST.get("email")
    otp= request.POST.get("otp")
    c=CustomerDetails1.objects.filter(email=email,otp=otp)
    if c:
        CustomerDetails1.objects.filter().update(status="Active")
        return render(request,"customer_template/customerapplication.html",{"msg":"Registration Successful"})
    else:
        return render(request, "customer_template/c_emailotp.html", {"msg": "Incorrect Emailid or Password"})
