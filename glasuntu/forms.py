from django import forms
from .models import ArtistPage
from .models import VenuePage

class ArtistPageForm(forms.ModelForm):
	class Meta:
		model = ArtistPage
		fields = ['name']
		labels = {'name': 'Name:'}
		
class VenuePageForm(forms.ModelForm):
	class Meta:
		model = VenuePage
		fields = ['name', 'address']
		labels = {'name': 'Name:',
				'address': 'Address:',
				}