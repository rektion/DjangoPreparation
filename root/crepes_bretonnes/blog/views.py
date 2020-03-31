from django.http import Http404
from django.shortcuts import render
from blog.models import Article
from django.shortcuts import render, get_object_or_404
from .forms import ArticleForm

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.

    form = ArticleForm(request.POST)
    if form.is_valid():
        form.save()
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/contact.html', locals())

def accueil(request):
    """ Afficher tous les articles de notre blog """
    return render(request, 'blog/accueil.html')