from django.urls import path
from . import views

urlpatterns = [
	path('accueil', views.accueil),
	path('article/<int:id_article>', views.view_article),
	path('redirection', views.view_redirection),
	path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
]