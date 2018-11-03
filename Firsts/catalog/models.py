from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter Genre')

    def __str__(self):
        return self.name
