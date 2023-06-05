from django.db import models
import time
from django.contrib.auth.models import AbstractUser

class administrator(AbstractUser):
    pass

class adherant(models.Model):
    matricule = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    date_naissance = models.DateTimeField()
    lieu_naissance = models.CharField(max_length=150)
    adresse = models.CharField(max_length=100)
    num_tel = models.IntegerField()

class livre(models.Model):
    code_livre = models.IntegerField(primary_key=True)
    auteur = models.CharField(max_length=200)
    titre = models.CharField(max_length=100)
    edition_liv = models.CharField(max_length=150)
    date_edit = models.DateTimeField()

class emprunt(models.Model):
    matricule = models.ForeignKey(adherant,on_delete=models.CASCADE, related_name="matricule_adherant")
    code_liv = models.ForeignKey(livre, on_delete=models.CASCADE, related_name="code_du_livre")
    date_emprunt = models.DateTimeField(auto_now=True)
    date_remis = models.DateTimeField()
    nb_exemp = models.IntegerField()