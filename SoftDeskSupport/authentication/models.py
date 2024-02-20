from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    can_be_contacted = models.BooleanField(default=False, verbose_name="Peux-etre contacté")
    can_be_shared = models.BooleanField(default=False, verbose_nmae = "Peut-être partagé")
    # TODO Termine l'implantation des champs comme password etc

"""class Contributor(User):
    project = models.ManyToManyField(Project)"""
