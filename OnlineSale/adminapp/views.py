from django.http import HttpResponse
from django.shortcuts import render
import random,json
# Create your views here.
from adminapp.models import Admin, Merchant, Product
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.core.serializers import serialize

def adminLogin(request):
    return render(request,"adminlogin.html")


def validate(request):
    uname=request.POST.get("uname")
    pwd=request.POST.get("pwd")
    p=Admin.objects.filter(username=uname,password=pwd)
    if p:
        return render(request,"adminwelcome.html",{"msg":"Welcome Admin"})
    else:
        return render(request,"adminlogin.html",{"msg":"Invalid Details"})


def addmerchant(request):
    return render(request,"addmerchant.html")


def viewmerchant(request):
    v=Merchant.objects.all()
    return render(request,"viewmerchant.html",{"data":v})


def deletemerchant(request):
    Merchant.objects.filter().delete()
    return render(request,"viewmerchant.html",{"msg":"Merchant Was Deleted"})


def addmc(request):
    id=random.randint(1000,9999)
    # x=Merchant.objects.all()
    # if x.id!=0:
    #     id1=x.id+1
    #
    # else:
    #     id1 = random.randint(1000, 9999)
    name=request.POST.get("name")
    cno=request.POST.get("cno")
    email=request.POST.get("email")
    pwd=random.randint(10000,99999)
    Merchant(id=id,name=name,contactno=cno,emailid=email,password=pwd).save()
    return render(request,"adminwelcome.html",{"msg":"Merchant Was added"})




@method_decorator(csrf_exempt,name='dispatch')
class Login(View):
    def post(self,request):
        data = request.body
        jd = json.loads(data)

        email=jd["emailid"]
        password=jd["password"]
        try:
            d=Merchant.objects.get(emailid=email, password=password)
            if d:
                jd = serialize('json',[d])
                return HttpResponse(jd, content_type="application/json")
        except:
            jd = json.dumps({"msg": "Invalid Details"})
            return HttpResponse(jd, content_type="application/json")

@method_decorator(csrf_exempt,name='dispatch')
class Addproduct(View):
    def post(self,request):
        data = request.body
        print(data)
        jd = json.loads(data)
        print(jd)
        no=jd["no"]
        name=jd["name"]
        price=jd["price"]
        quantity=jd["quantity"]
        mid=jd["mid"]

        print(jd["no"])
        ef=Product(no=no,name=name,price=price,quantity=quantity,mid_id=mid).save()

        js = json.dumps({"msg": "product is saved"})
        return HttpResponse(js, content_type="application/json")

@method_decorator(csrf_exempt,name='dispatch')
class Changepwd(View):
    def post(self,request):
        data = request.body
        print(data)
        jd = json.loads(data)
        print(jd)
        email=jd['email']
        old=jd['old']

        new=jd['new']
        confirm=jd['confirm']
        if new==confirm:
            p=Merchant.objects.filter(emailid=email,password=old).update(password=confirm)
            print(p)
        else:
            js = json.dumps({"msg": "False"})
            return HttpResponse(js, content_type="application/json")
        if p:
            js = json.dumps({"msg": "password changed"})
            return HttpResponse(js, content_type="application/json")
        else:
            js = json.dumps({"msg": "0"})
            return HttpResponse(js, content_type="application/json")


class Viewproduct(View):
    def get(self,request):
        qs=Product.objects.all()
        jd=serialize("json",qs,fields=('no','name','price','quantity'))
        print(jd)

        return HttpResponse(jd,content_type="application/json")
@method_decorator(csrf_exempt, name="dispatch")
class UpdateProduct(View):
    def get(self,request,pk):
        olddata = Product.objects.filter(no=pk)
        print(olddata)
        # olddatadic={"name":olddata.name,"price":olddata.price,"quantity":olddata.quantity}
        # print(olddatadic)
        jd = serialize("json", olddata, fields=('no', 'name', 'price', 'quantity'))
        print(jd)
        return HttpResponse(jd, content_type="application/json")



    def put(self,request):
        data=request.body
        newdata=json.loads(data)
        print(newdata)
        olddata=Product.objects.get(no=newdata['no'])
        print(olddata)
        olddict={'no':olddata.no,'name':olddata.name,'price':olddata.price,'quantity':olddata.quantity}
        print(olddict)
        k=olddict.update(newdata)
        print(k)
        ef=Product(olddict,instance=olddata)
        # if ef.is_valid():
        ef.save()
        print(ef)
        return HttpResponse(status=200)

@method_decorator(csrf_exempt, name="dispatch")
class DeleteProduct(View):
    def delete(self,request,pno):
        Product.objects.get(no=pno).delete()
        return HttpResponse(status=200)

