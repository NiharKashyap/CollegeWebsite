from . import views
from django.urls import path

urlpatterns = [
    path('registration/', views.register),
    path('feedback/', views.feeds ),
    path('login/',views.login),
    path('', views.index),
    path('PutDetails/<username>/',views.Put_Details),
    path('bscit/',views.bscit),
    path('notice/',views.notice),
    path('bsc/', views.bsc),
    path('msc/', views.msc),
    path('engg/', views.engg),
    path('logout/', views.logout)
]