from django.db import models

# Create your models here.
class Brainstrom(models.Model):
    id =models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50 , verbose_name = 'Kullanıcı adı')
    description = models.TextField(verbose_name = "Açıklama")
    image = models.CharField(max_length = 25 , verbose_name="Görsel")
    created_date = models.DateTimeField(auto_now_add = True ,verbose_name = "Olay vakti")

    isPublished = models.BooleanField(default = True)

    def __str__(self):
        return self.name #isim dönerir movie object yerine
    
    def get_image_path(self):
        return '/img/' + self.image

    #def save(self,*args,**kwargs):
     #   super().save(*args,**kwargs)
