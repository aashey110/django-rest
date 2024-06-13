from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    duration = models.IntegerField(null = True, blank=False)
    image = models.ImageField(upload_to='recipe_images/', null=True, blank= True)