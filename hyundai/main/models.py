from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name
