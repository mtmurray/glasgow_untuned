from django.db import models

# Create your models here.
class VenuePage(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	def __str__(self):
		return self.text

class ArtistPage(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.text
		
class Genre(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.text
		
class Event(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.text