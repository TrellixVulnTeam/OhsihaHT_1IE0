from django.db import models
from django.contrib.auth.models import User

class Profiles(models.Model):
    """Käyttäjäprofiilien tallennus"""
    #username = models.CharField(max_length=50)
    #miten varmistetaan ettei useampaa samaa, SQL:n avula DB:stä, ID:n avulla?
    #email = models.CharField(max_length=50)
    #firstname = models.CharField(max_length=50)
    #lastname = models.CharField(max_length=50)

class Document(models.Model):
    selite = models.CharField(max_length=250, blank = True)
    #palauttaja = models.ForeignKey(User)
    palautusaika = models.DateTimeField(auto_now_add=True)
    korvausdokumentti = models.FileField(upload_to='korvaukset/')

#MUISTA, DJANGO LUO ID:N AUTOMAATTISESTI

# Create your models here.
