from django.db import models

# Create your models here.


class Profiles(models.Model):
    title = models.CharField(max_length = 80)
    created_by = models.CharField(max_length = 35)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

