from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.conf import settings
# Create your views here.
def login(request):

    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        user1 = auth.authenticate(username = username1 , password = password1)
        
        if user1 is not None:
            auth.login(request , user1)
            return render(request,'pages/index.html') #index nameli sayfaya yolluyor
        else:
            messages.add_message(request,messages.ERROR,'Hatalı kullanıcı adı veya parola')
            return redirect('login')


    else:
        return render(request,'user/login.html')

            


   

def register(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        email1 = request.POST['email']
        password1 = request.POST['password']
        
        if User.objects.filter(username = username1).exists():
            messages.add_message(request, messages.WARNING,'Bu kullanıcı adı daha önceden alınmış.')
            return redirect('register')

        else:
            if User.objects.filter(email = email1).exists():
                messages.add_message(request, messages.WARNING,'Bu email daha önce kullanılmış.')
                return redirect('register')

            else:
                user = User.objects.create_user(username = username1 , password = password1 , email = email1)
                user.save()
                messages.add_message(request, messages.WARNING,'Kayıt işlemi tamamlandı.') #message frameworkü kullanıyorum başarılı giriş olduguna dair mesaj vericek
                return redirect('login')
    else:
        return render(request , 'user/register.html')


def logout(request):
    auth.logout(request)
    messages.add_message(request , messages.SUCCESS,'Çıkış başarılı. Oturum kapandı.')
    return redirect('index')
