from django.db import models

# pokedex_app/models.py

from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    stats = models.TextField()
    
    def __str__(self):
        return self.name

