from django.shortcuts import render #render function is responsible for rendering the info in the views
from django.core.urlresolvers import reverse
from django.db.models import Q
from .models import VenuePage
from .models import Event
from .models import Genre
from .models import ArtistPage
from .forms import ArtistPageForm, VenuePageForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
	events = Event.objects.filter(venue=venue)
	id = venue.id
	context_dict = {
		"venue":venue,
		"events":events,
		"id":id,
	}
	
	return render(request, 'glasuntu/venue.html', context_dict)
	
def artist(request, artist_id):
	artist = ArtistPage.objects.get(id=artist_id)
	artistName = artist.name
	id = artist.id
	
	context_dict = {
		"artist":artist,
		"id":id,
	}
	
	return render(request, 'glasuntu/band.html', context_dict)
	
@login_required
def new_artist(request):
	if request.method != 'POST':
		form = ArtistPageForm()
	else:
		form = ArtistPageForm(data = request.POST)
		if form.is_valid():
			new_artist = form.save(commit=False)
			new_artist.owner = request.user
			new_artist.save()
			
	context_dict = {'form':form}
	return render(request, 'glasuntu/new_artist.html', context_dict)
	
@login_required
def new_venue(request):
	if request.method != 'POST':
		form = VenuePageForm()
	else:
		form = VenuePageForm(data = request.POST)
		if form.is_valid():
			new_venue = form.save(commit=False)
			new_venue.owner = request.user
			new_artist.save()
			
	context_dict = {'form':form}
	return render(request, 'glasuntu/new_venue.html', context_dict)
	
def edit_artist(request, artist_id):
	artist = ArtistPage.objects.get(id=artist_id)
	info = artist.info
	
	if request.method != 'POST':
		form = ArtistPageForm(instance=artist)
	else:
		form = ArtistPageForm(instance=artist, data=request.POST)
		if form.is_valid():
			form.save()
			
	context_dict = {'artist':artist, 'info':info, 'form':form, 'id':artist_id}
	return render(request, 'glasuntu/edit_artist.html', context_dict)

def edit_venue(request, venue_id):
	venue = VenuePage.objects.get(id=venue_id)
	info = venue.info
	
	if request.method != 'POST':
		form = VenuePageForm(instance=venue)
	else:
		form = VenuePageForm(instance=venue, data=request.POST)
		if form.is_valid():
			form.save()
			
	context_dict = {'venue':venue, 'info':info, 'form':form, 'id':venue_id}
	return render(request, 'glasuntu/edit_venue.html', context_dict)
	
def register(request):
	registered = False
	
	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
		
			profile = profile_form.save(commit=False)
			profile.user = user
		
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
				
			profile.save()
		
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
		
	return render(request,
        'glasuntu/register.html',
        {'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered})
		
def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('glasuntu:index'))
			else:
				return HttpResponse("Your Glasgow Untuned account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")

	else:
		return render(request, 'glasuntu/login.html', {})
		
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('glasuntu:index'))

