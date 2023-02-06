from django.contrib.auth.models import AbstractUser
from django.db import models


class Author(AbstractUser):
    pass

    def __str__(self):
        return self.username

