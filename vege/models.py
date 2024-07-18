from django.db import models

class Recipe(models.Model):
    receipe_name = models.CharField(default="", max_length=100)
    receipe_description = models.TextField(default="")
    receipe_image = models.ImageField(upload_to='receipe')
