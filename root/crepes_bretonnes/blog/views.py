from django.http import Http404
from blog.models import Article
from django.shortcuts import render, get_object_or_404
from .forms import ArticleForm
from .forms import NouveauContactForm
from .models import Contact as C

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


def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True

    return render(request, 'blog/contact.html', {
        'form': form, 
        'sauvegarde': sauvegarde
    })

def voir_contacts(request):
    return render(
        request, 
        'blog/voir_contacts.html', 
        {'contacts': C.objects.all()}
    )