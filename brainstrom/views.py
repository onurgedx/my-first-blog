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
            


        brainstrom = Brainstrom.objects.filter( baglanti = None)
        brainstrom =brainstrom[::-1] #bu şekilde en son yazan en son geliyor listeyi ters çevirdim işte 
        context = {
            'brainstrom' : brainstrom
        }
        return render(request,'brainstrom/brainstrom.html',context)
    
    else:
        messages.add_message(request , messages.WARNING ,'Bu sayfayı görebilmek için giriş yapmalısınız.Giriş yapabilmek için ise kayıt olmalısınız.')

        return render(request,'user/register.html')

def rush(request,rush_id): #burda rush id yi belirttim pk yi rush_id ye eşitledm
    
#BURDA ÇOK PROBLEM YAŞADIM PROBLEMİM  BU YANIT YAZMAK İÇİN OLAN YERDE form action için bir id yollamıyor olmam
   
    if request.user.is_authenticated:
       
        
        if request.method == 'POST':
           
          
            username3 = request.user.username
            description3 = request.POST['descriptionRush']
            Brainstrom.objects.create(name = username3 ,description = description3 , baglanti = rush_id )
        else: 
            if  Brainstrom.objects.filter( baglanti = rush_id).exists() == False:
                username3 = 'else'
                description3 = 'else'
                Brainstrom.objects.create(name = username3 ,description = description3 , baglanti = rush_id )
        brainstrom = get_object_or_404(Brainstrom , pk = rush_id)
        
        rush = Brainstrom.objects.filter( baglanti = rush_id)
        rush = rush[::-1]                

        context = {'rush': rush,
        'brainstrom' : brainstrom,
                    } 
        return render(request,'brainstrom/rush.html',context)
       
    else:
        messages.add_message(request , messages.WARNING ,'Bu sayfayı görebilmek için giriş yapmalısınız.Giriş yapabilmek için ise kayıt olmalısınız.')

        return render(request,'user/register.html')
        

def search(request):
    return render(request,'brainstrom/search.html')