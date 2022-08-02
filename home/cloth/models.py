from operator import length_hint
from django.db import models
from django.conf import settings

# Create your models here.
class Enroll(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length = 200)
    zip_code = models.CharField(max_length = 5)
    user_id = models.CharField(max_length = 20)
    password = models.CharField(max_length = 10)
    email = models.CharField(max_length = 20)
    phone = models.CharField(max_length = 11)
    created_date = models.DateTimeField()

