from django.db import models

from django.db.models.signals import pre_delete, post_save, pre_save
from django.dispatch import receiver

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()

    def __str__(self):
        return self.title
    
   