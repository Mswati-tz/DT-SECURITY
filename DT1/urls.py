from django.urls import path
from . import views

urlpatterns = [
    # Kurasa za Kawaida (HTML)
    path('', views.home, name="home"),
    path('About_us/', views.about, name="about"),
    path('Our_client/', views.client, name="client"),
    path('Our_Services/', views.services, name="services"),
    path('Contact_us/', views.contact, name="contact"), # Imeboreshwa spelling
    path('Updates/', views.update, name="updates"),
    path('Apply/', views.apply, name="apply"), # Imepewa path yake ya kipekee

    
]
