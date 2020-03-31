from django.urls import path
from . import views

urlpatterns = [
	path('accueil', views.accueil),
	path('contact/', views.contact, name='contact'),
]