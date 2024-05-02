from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"
  

class Ejer(models.Model):
  Ejer_navn = models.CharField(max_length=255)
  Ejer_efternavn = models.CharField(max_length=255)
  Ejer_email = models.CharField(max_length=255)
  Ejer_Telefon = models.IntegerField(null=True)


class Sommerhus(models.Model):
  Adresse = models.CharField(max_length=255)
  Ejer_id = models.IntegerField(null=True)
  Plads_til = models.IntegerField(null=True)

  