from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('About_us',views.about,name="about"),
    path('Our_client',views.client,name="client"),
    path('Our_Services',views.services,name="services"),
    path('Contuct_us',views.contact,name="contact"),
    path('Updates',views.update,name="updates"),
    path('Updates',views.apply,name="apply"),
    
    path('contact/', views.contact, name='contact'), # Hakikisha name='contact' ipo hapa


    path('contact/', views.contact, name='contact'), # Hii ni ile page ya HTML
    path('api/messages/', views.ContactMessageListAPI.as_view()), # Hii ni API ya kuona meseji hizo hizo

    # --- HIZI NDIO NJIA MPYA ZA API ---
    path('api/askari/', views.AskariListCreateAPI.as_view(), name='askari-api'),
    path('api/reports/', views.ReportListCreateAPI.as_view(), name='reports-api'),

]
