"""This file outlines the url patterns for Glasgow Untuned ('glasuntu')"""

from django.conf.urls import url #url function connects urls to views
from . import views

#urlpatterns contains list of page urls for Glasgow_Untuned
urlpatterns = [
	#Home - url function takes 3 arguments: regular expression (r'^$'), function to be called (views.index), url pattern name (index)
	url(r'^$', views.index, name='index'),
	
	#List - display search results
	url(r'^list/$', views.search, name='search'),
	
	#Artist page url
	url(r'^band/(?P<artist_id>\d+)/$', views.artist, name='artist'),
	
	#Venue page url
	url(r'^venue/(?P<venue_id>\d+)/$', views.venue, name="venue"),
]