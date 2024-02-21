from django.urls import path
from MyApp import views

urlpatterns=[

    path('karibu/', views.karibu),
    path('', views.home, name='my_index'),
    path('about/', views.about, name='my-about'),
    path('contact/', views.contactus, name='my-contact'),
    path('gallery/', views.gallery, name='my_gallery'),
    path('services/', views.services, name='my-services'),

]