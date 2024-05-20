# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    cover_photo = models.ImageField(upload_to='images/', null=True, blank=True)  # Add this line
    status = models.BooleanField(default=True)  # Add the status field with default value

    def __str__(self):
        return self.title
