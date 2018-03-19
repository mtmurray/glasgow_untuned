import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'glasgow_untuned.settings')

import django
django.setup()
from glasuntu.models import VenuePage, Event

def populate():
    a=VenuePage(id=1,
    name="Barrowland Ballroom",
    address="244 Gallowgate, Glasgow G4 0TT",
    picture="https://media.timeout.com/images/101789263/image.jpg",
    website="http://www.glasgow-barrowland.com/ballroom.htm",
    info="Barrowland Ballroom is a dance hall and music venue located in Gallowgate.  Inside the famous neon sign you will find hot food, a packed bar and live music from some of the finest bands around.",
    genre="Indie, Rock")

    
    b=VenuePage(id=2,
    name="O2 ABC Glasgow",
    address="300 Sauchiehall St, Glasgow G2 3JA",
    picture="http://2.bp.blogspot.com/-1cIOiQe-d4M/UaTfb6dtWkI/AAAAAAAAG_M/MDu-PVYMc44/s1600/O2ABC1_fused-2k.jpg",
    website="https://academymusicgroup.com/o2abcglasgow/",
    info="The O2 ABC is a nightclub and music venue on Sauchiehall Street, in the centre of Glasgow.  Averaging over 400 events annually, it is one of Glasgow’s most iconic and respected venues and has made a huge contribution to the live music scene.",
    genre="Rock, Dance, House, Indie")     
    a.save()
    b.save()

    c=Event(name="The Killers", date="20/05/18", venue=a)
    d=Event(name="Kasabian", date="27/05/18", venue=a)
    e=Event(name="Made up band", date="23/05/18", venue=b)
    f=Event(name="Made up band", date="30/05/18", venue=b)
    c.save()
    
    d.save()
    e.save()
    f.save()



    
if __name__=='__main__':
    print("populating")
    populate()