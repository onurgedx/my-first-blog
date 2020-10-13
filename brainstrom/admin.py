from django.contrib import admin
from .models import Brainstrom
# Register your models here.



class BrainstromAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_date','isPublished','description')
    list_disply_links = ('id','name')
    list_filter = ('created_date',)
    list_editable = ('isPublished',)
    search_fields = ('name','description','created_date')
    list_per_page = 10

admin.site.register(Brainstrom,BrainstromAdmin)