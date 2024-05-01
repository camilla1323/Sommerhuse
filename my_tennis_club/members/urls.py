from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('ejer/', views.ejer, name='ejer'),
    path('ejer/details/<int:id>', views.detailsejer, name='detailsejer'),
    path('sommerhus/',views.sommerhus, name='sommerhus'),
    path('sommerhus/details/<int:id>',views.detailssommerhus, name='details'),
]   