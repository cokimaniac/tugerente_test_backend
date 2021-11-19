from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Client(AbstractBaseUser):
    email = models.EmailField(
        "email address",
        unique=True,
        error_messages={
            "unique": "This email is been using for other user"
        }
    )
    first_name = models.CharField(
        "first name",
        max_length=70,
        blank=True
    )
    last_name = models.CharField(
        "last name",
        max_length=80,
        blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]
    
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def str(self):
        return self.username

