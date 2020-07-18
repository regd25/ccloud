"""Utils models"""
#Django
from django.contrib.auth.models import AbstactUser
from dajgo.db import models

class CCmodel (AbstactUser):
    """ This class define a abstract class for add created and updated fields to requiered models"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        abstract = True