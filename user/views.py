from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def register(request):
    form = UserForm()
    if request.method =='POST':
        form = UserForm(request.POST)#formdan gelen mesajları yazdırır.
        # print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Başarılı bir şekilde kayıt oldunuz. Aramıza hoş geldiniz')
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'register.html', context)


def userLogin(request):
    if request.method=='POST':        
        kullanici = request.POST.get('kullanici')
        sifre = request.POST.get('sifre')
        user= authenticate(request, username = kullanici, password = sifre)
        if user is not None:
            login(request, user)
            messages.success(request,'Giriş Yapıldı')
            next= request.GET.get('next')#girişli değilken ulaşmaya çalıştığı sayfaya yönlendirmek için
            if next:
                return redirect(next)
            else:
                return redirect('index')
            
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı')
            return redirect('login')
        
    return render(request, 'login.html')
    
def userLogout(request):
    logout(request)
    messages.success(request, 'çıkış yaptınız. Tekrar bekleriz.')
    return redirect('index')
