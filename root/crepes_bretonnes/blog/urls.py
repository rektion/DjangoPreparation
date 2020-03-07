from django.urls import path
from . import views

urlpatterns = [
	path('accueil', views.home),
	path('article/<int:id_article>', views.view_article),
	path('redirection', views.view_redirection),
]