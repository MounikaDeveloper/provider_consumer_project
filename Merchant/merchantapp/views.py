from django.shortcuts import render
import json

# Create your views here.
def merchantHome(request):
    return render(request,"merchanthome.html")


def product(request):
    return render(request,"product.html")

def login(request):
    uname = request.POST.get("uname")
    password = request.POST.get("pwd")
    d1 = {"emailid": uname, "password": password}
    json_data = json.dumps(d1)
    print(json_data)
    res = requests.post("http://127.0.0.1:3000/login/", data=json_data)
    print(res.status_code)
    print(res.json())
    data=res.json()
    print(data)
    # if data['msg']== "Invalid Details":
    #     return render(request,"merchanthome.html",{"msg":"Invalid Login"})

    return render(request,"addproduct.html",{"Data":res.json()})


def saveproduct(request):
    pno=request.POST.get("pno")
    mid = request.POST.get("mid")
    name=request.POST.get("pname")
    price=request.POST.get("price")
    quant=request.POST.get("quant")
    d={"no":pno,"name":name,"price":price,"quantity":quant,"mid":mid}
    print(d)
    json_data=json.dumps(d)
    print(json_data)

    res=requests.post("http://127.0.0.1:3000/addproduct/",data=json_data)
    print(res.status_code)
    print(res.json())

    return render(request,"product.html",{"msg":"Product is Saved"})





def changepassword(request):
    email=request.POST.get("email")
    old=request.POST.get("old")
    new=request.POST.get("new")
    confirm=request.POST.get("confirm")
    d={"email":email,"old":old,"new":new,"confirm":confirm}
    json_data=json.dumps(d)
    res=requests.post("http://127.0.0.1:3000/changepwd/",data=json_data)
    print(res)
    print(res.status_code)
    print(res.json())
    d=res.json()
    msg=d['msg']
    print(msg)
    if msg=='0':
        return render(request,"merchanthome.html",{"msg":"EmailID or password are incorrect"})
    if msg=='False':
        return render(request,"merchanthome.html",{"msg":"New Password and confirm password are not same"})
    else:
        return render(request,"merchanthome.html",{"msg":"Password Changed"})


import requests
from django.views.generic import View
# class Readone(View):
#     def get(self,request):
#         try:
#             res=requests.get("http://127.0.0.1:3000/readone")
#             print(res.status_code)
#             print(res.json())
#         except requests.exceptions.ConnectionError:
#             print("server not available")

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
def loginCheck(self,request):
        uname = request.POST.get("uname")
        print(uname)
        password=request.POST.get("pwd")
        d1={"emailid":uname,"password":password}
        print(d1)
        json_data=json.dumps(d1)
        print(json_data)
        res = requests.post("http://127.0.0.1:3000/writeone/",data=json_data)
        print(res.status_code)
        print(res.json())
        return None





def change(request):
    return render(request,"changepassword.html")


def addproduct(request):
    return render(request,"addproduct.html")


def viewproduct(request):
    res=requests.get("http://127.0.0.1:3000/viewproduct")
    print(res.status_code)
    print(res.json())
    d=res.json()
    return render(request,"viewproduct.html",{"data":d})


def updateproduct(request):
    id=request.GET.get("pid")
    res = requests.get("http://127.0.0.1:3000/updateproduct/"+id+"/")
    print(res)
    print(res.status_code)
    print(res.json())
    d = res.json()
    return render(request,"updateproduct.html",{"data":d})


def upd_prod(request):
    no=request.POST.get("no")
    name=request.POST.get("name")
    price=request.POST.get("price")
    quantity=request.POST.get("quantity")
    d={"no":no,"name":name,"price":price,"quantity":quantity}
    jd=json.dumps(d)
    print(jd)
    res=requests.put("http://127.0.0.1:3000/updateprod/",data=jd)
    # print(res.json())
    if res.status_code==200:

        return render(request,"product.html",{"msg":"Data Updated"})
    else:
        return render(request, "product.html", {"msg": "Data not Updated"})


def deleteproduct(request):
    pid=request.GET.get("pid")
    res = requests.delete("http://127.0.0.1:3000/deleteproduct/" + pid + "/")

    print(res)
    print(res.status_code)
    # print(res.json())
    if res.status_code==200:
        return render(request,"viewproduct.html",{"data":'Product was deleted'})