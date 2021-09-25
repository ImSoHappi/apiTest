from django.db import models

# Create your models here.

class messageModel(models.Model):
    messages = models.CharField(max_length=200)

    def __str__(self):
        return self.messages