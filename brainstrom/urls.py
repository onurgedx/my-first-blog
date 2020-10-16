from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='brainstrom'),
    path('<int:rush_id>', views.rush ,name='rush'),
    path('search', views.search ,name='search'),
]