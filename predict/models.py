from email.policy import default
from django.db import models

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=50)
    grade = models.IntegerField(default=3)

    def __str__(self):
        return self.client_name