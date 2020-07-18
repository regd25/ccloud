"""User app models"""

#Django
from django.contrib.auth.models import AbstractUser
from django.db import modles
from django.core.validators import RegexValidator

#CCloud
from crasterras_cloud.utils.models import CCmodel


class User(CCmodel, AbstractUser):
    """Extrends form AbstractUser, change the user field to email and add some extra fields"""

    email = models.EmailField(
        'email adress'
        unique=True,
        error_messages={
            'unique':'A user with that email already exists'
        }
    )
    phone_number =models.CharField(max_length=17)

    USERNAME_FIELD='email'
    REQUIERED_FIELDS=['first_name', 'last_name']

    def __str__(self):
        return self.email   


