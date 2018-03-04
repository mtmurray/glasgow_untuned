"""This file outlines the url patterns for Glasgow Untuned ('glasuntu')"""

from django.conf.urls import url #url function connects urls to views
from . import views

#urlpatterns contains list of page urls for Glasgow_Untuned
urlpatterns = [
	#Home - url function takes 3 arguments: regular expression (r'^$'), function to be called (views.index), url pattern name (index)
	url(r'^$', views.index, name='index'),
]