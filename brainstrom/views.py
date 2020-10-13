from django.shortcuts import render
from django.shortcuts import get_object_or_404 #çok basit ve tatlı obje varsa objeye götürüyor yoksa 404 sayfasına
from django.http import Http404 # hata olunca   kullanmak için Http404 hatasını import ediyoruz
from .models import Brainstrom
from django.contrib import messages
# Create your views here.


def index(request):
    if request.user.is_authenticated: #sonuna parantez koymayınca çalıştı
        
        if request.method == 'POST':
            #usernamesinialır şşuanki kullanıcnın
            #print(User.get_username())
            #https://stackoverflow.com/questions/16906515/how-can-i-get-the-username-of-the-logged-in-user-in-django
            #burdan buldum alltakini
            """
            def my_view(request):
                username = None
                if request.user.is_authenticated(): #parantezler olmayınca daha iyi çalıştı
                    username = request.user.username
            """
            username2 = request.user.username#ŞU ANKİ KULLANICININ İSMİNİ ALMA İŞLEMİ
            

            description2 = request.POST['description']
            
            Brainstrom.objects.create(name = username2 ,description= description2)


        brainstrom = Brainstrom.objects.all()
        context = {
            'brainstrom' : brainstrom
        }
        return render(request,'brainstrom/brainstrom.html',context)
    
    else:
        messages.add_message(request , messages.WARNING ,'Bu sayfayı görebilmek için giriş yapmalısınız.Giriş yapabilmek için ise kayıt olmalısınız.')

        return render(request,'user/register.html')