from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    can_be_contacted = models.BooleanField(default=False, verbose_name="Peux-etre contacté")
    can_be_shared = models.BooleanField(default=False, verbose_name = "Peut-être partagé")
    age = models.PositiveIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='base_users',
        blank=True,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='base_users_permissions',
        blank=True,
        verbose_name='user permissions',)
    
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
