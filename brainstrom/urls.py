from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='brainstrom'),
    #path('<int:movie_id>', views.detail ,name='detail'),
    #path('search', views.search ,name='search'),
]