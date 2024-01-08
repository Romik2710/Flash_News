from django.db import models
from django.core.exceptions import ValidationError


# Create your models here


class UserData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def clean(self):
        """
        Custom validation for the model fields.
        """
        if self.password1 != self.password2:
            raise ValidationError("Passwords do not match.")
