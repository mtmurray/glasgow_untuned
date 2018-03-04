from django.shortcuts import render #render function is responsible for rendering the info in the views

def index(request):
	"""Glasgow Untuned home page"""
	return render (request, 'glasuntu/index.html')
