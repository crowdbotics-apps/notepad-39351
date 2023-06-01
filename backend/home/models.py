from django.conf import settings
from django.db import models
class Test(models.Model):
    'Generated Model'
    location = models.BigIntegerField()
    name = models.BigIntegerField()
