from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=28)
    last_name = models.CharField(max_length=28)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        db_table = 'adani_users'

    def __str__(self):
        return self.get_full_name()
