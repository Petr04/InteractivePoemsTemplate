from django.db import models

# Create your models here.
class Poem(models.Model):
	ended = models.BooleanField(default=False)

class Paragraph(models.Model):
	poem = models.ForeignKey(
		Poem,
		on_delete=models.CASCADE,
	)
	author = models.CharField(max_length=16)
	text = models.TextField()
	last = models.BooleanField(default=False)
