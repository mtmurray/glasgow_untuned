from django.shortcuts import render #render function is responsible for rendering the info in the views
from django.db.models import Q
from .models import VenuePage
from .models import Event
from .models import Genre

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
	query = request.GET.get("q")
	
	queries = VenuePage.objects.filter(
		Q(name__icontains=query)
	)
		
	context_dict = {
		"queries":queries,
	}
	
	return render (request, "glasuntu/list.html", context_dict)
	
def venue(request, venue_id):
	venue = VenuePage.objects.get(id=venue_id)
	venueName = venue.name
	context_dict = {
		"venue":venueName,
	}
	
	return render(request, 'glasuntu/venue.html', context_dict)