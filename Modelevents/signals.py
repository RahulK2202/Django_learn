# signals.py

from django.db.models.signals import pre_delete, post_save, pre_save,post_delete
from django.dispatch import receiver
from django.db import models
from .models import Book

@receiver(post_save, sender=Book)
def post_save_book(sender, instance, created, **kwargs):
    print
    print("signal started ")
    print("instance",instance)
    print(created,"created")
    print(sender,"sender")
    if created:
        print(f"New book created with ID: {instance.id}")
    else:
        print(f"Book updated with ID: {instance.id}")

@receiver(post_delete, sender=Book)
def post_delete_handler(sender, instance, **kwargs):
    # Your post_delete signal handling logic here
    print("post delete started")
    print(sender,"sender got")
    print(instance,"instance")
    print("signal completed")
    print("........................................................")

    print(f"Deleted instance with ID: {instance.id}")
