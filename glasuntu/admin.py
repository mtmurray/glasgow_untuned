from django.contrib import admin
from .models import VenuePage
from .models import Genre
from .models import ArtistPage
from .models import Event

# Register your models here.
admin.site.register(VenuePage)
admin.site.register(Genre)
admin.site.register(ArtistPage)
admin.site.register(Event)
