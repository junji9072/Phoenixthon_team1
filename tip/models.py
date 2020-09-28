from django.db import models

# Create your models here.
class Items(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 50)
    description = models.TextField()

    def __str__(self):
        return self.name