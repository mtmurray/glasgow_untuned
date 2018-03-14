from django.db import models

# Create your models here.
class VenuePage(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class ArtistPage(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name
		
class Genre(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name
		
class Event(models.Model):
	name = models.CharField(max_length=150)
	date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name