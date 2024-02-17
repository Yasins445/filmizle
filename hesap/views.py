from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login 
# Create your views here.

def giris_request(request):
    if request.method == "POST":
       kullanici_adi= request.POST["kullanici_adi"]
       sifre = request.POST["sifre"]
       user =  authenticate(request, kullanici_adi = kullanici_adi, sifre=sifre)

       if user is not None:
            login(request,user)
            return  redirect("index")
       else:
           return render(request, "hesap/giris.html",{
                      "error": "kullanıcı adı ya da şifre hatalı"})


    return render(request,"hesap/giris.html")


def kaydol_request(request):
    
    return render(request,"hesap/kaydol.html")



def cik_request(request):
    return redirect("home")