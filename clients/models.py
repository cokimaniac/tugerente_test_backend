from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class ClientManager(BaseUserManager):

    def create_user (self, email, password=None):
        if not email:
            raise ValueError("Client user must be linked with email")

        client = self.model(
            email=self.normalize_email(email),
        )
        client.is_staff = False
        client.set_password(password)
        client.save(using=self._db)
        return client

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

    objects = ClientManager()
    
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email

