from django.shortcuts import render #render function is responsible for rendering the info in the views
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Q
from .models import VenuePage
from .models import Event
from .models import Genre
from .models import ArtistPage
from .forms import ArtistPageForm
from .forms import VenuePageForm

def index(request):
	"""Glasgow Untuned home page"""
	events = Event.objects.order_by('date')
	genres = Genre.objects.order_by('name')
	
	context_dict = {
		"events":events,
		"genres":genres,
	}
	
	return render (request, 'glasuntu/index.html', context_dict)

	
def search(request):
	#retrieve user's query (q) and the desired search type (s)
	query = request.GET.get("q")
	search_type = request.GET.get("s") #search_type will contain "value" attribute of selected <option>
	queries = ""
	view = ""
	
	#get data depending on contents of <select> menu in base.html
	if search_type == "v":
		queries = VenuePage.objects.filter(
			Q(name__icontains=query)
		)
		view = "venue"	
	elif search_type == "a":
		queries = ArtistPage.objects.filter(
			Q(name__icontains=query)
		)
		view = "artist"
		
	context_dict = {
		"queries":queries,
		"view":view,
	}
	
	return render (request, "glasuntu/list.html", context_dict)
	
def venue(request, venue_id):
	venue = VenuePage.objects.get(id=venue_id)
	venueName = venue.name
	context_dict = {
		"venue":venueName,
	}
	
	return render(request, 'glasuntu/venue.html', context_dict)
	
def artist(request, artist_id):
	artist = ArtistPage.objects.get(id=artist_id)
	artistName = artist.name
	
	context_dict = {
		"artist":artistName,
	}
	
	return render(request, 'glasuntu/band.html', context_dict)
	
def new_artist(request):
	if request.method != 'POST':
		form = ArtistPageForm()
	else:
		form = ArtistPageForm(data = request.POST)
		if form.is_valid():
			form.save()
			
	context_dict = {'form':form}
	return render(request, 'glasuntu/new_artist.html', context_dict)
	
def new_venue(request):
	if request.method != 'POST':
		form = VenuePageForm()
	else:
		form = VenuePageForm(data = request.POST)
		if form.is_valid():
			form.save()
			
	context_dict = {'form':form}
	return render(request, 'glasuntu/new_venue.html', context_dict)