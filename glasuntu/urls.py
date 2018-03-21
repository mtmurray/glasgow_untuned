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
	
	#Create artist page url
	url(r'^new_artist/$', views.new_artist, name = 'new_artist'),
	
	#Register venue page url
	url(r'^new_venue/$', views.new_venue, name = 'new_venue'),
	
	#User registration url
	url(r'^register/$', views.register, name='register'),
	
	#User login url
    url(r'^login/$', views.user_login, name='login'),
	
	#Logout page url
    url(r'^logout/$', views.user_logout, name='logout'),
	
	#Edit artist description url
	url(r'^edit_artist/(?P<artist_id>\d+)/$', views.edit_artist, name='edit_artist'),
	
	#Edit venue description url
	url(r'^edit_venue/(?P<venue_id>\d+)/$', views.edit_venue, name='edit_venue'),

        #likes
        url(r'^like_venue/$', views.like_venue, name='like_venue'),
]
