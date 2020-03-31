from django.db import models
from django.utils import timezone

class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom	

class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    slug = models.SlugField(max_length=100)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie',on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.titre