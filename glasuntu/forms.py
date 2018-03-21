from django import forms
from .models import ArtistPage
from .models import VenuePage
from .models import UserProfile
from django.contrib.auth.models import User

class ArtistPageForm(forms.ModelForm):
	class Meta:
		model = ArtistPage
		fields = ['name', 'website', 'info', 'genre']
		labels = {'name': 'Name:',
					'website': 'Website:',
					'info':'Description:',
					'genre':'Genre(s):'}
		widgets = {'info': forms.Textarea(attrs={'cols': 50})}
		
class VenuePageForm(forms.ModelForm):
	class Meta:
		model = VenuePage
		fields = ['name', 'address', 'website', 'info', 'genre']
		labels = {'name': 'Name:',
				'address': 'Address:',
				'website': 'Website:',
				'info':'Description:',
				'genre':'Genre(s):'
				}
		widgets = {'info': forms.Textarea(attrs={'cols': 50})}
		
class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture',)
