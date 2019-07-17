from django.db import models

# Create your models here.
class Poem(models.Model):
    text = models.TextField()
    ended = models.BooleanField(default=False)