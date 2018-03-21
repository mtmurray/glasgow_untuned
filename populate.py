import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'glasgow_untuned.settings')

import django
django.setup()
from glasuntu.models import VenuePage, Event, ArtistPage
from glasuntu.models import User, UserProfile
def populate():
    user = User.objects.get_or_create(username="firstuser", password="test1234",
                                        email="startuser@gmail.com")[0]
    user.set_password(user.password)
    

    # Create a user profile
    user_profile = UserProfile.objects.get_or_create(user=user)[0]
    user_profile.save()

    
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


    kill=ArtistPage(id=1,
    name="The Killers",
    picture="https://metrouk2.files.wordpress.com/2017/01/the-killers-2-e1485012869982.jpg?quality=80&strip=all&strip=all",
    website="http://www.thekillersmusic.com/",
    info="The Killers are an American rock band formed in Las Vegas, Nevada, in 2001.  The Killers are seen as one of the biggest rock bands of the 21st century, and the most successful to ever emerge from Nevada, having sold an estimated 22 million records worldwide",
    genre="Rock")
    
    kas=ArtistPage(id=2,
    name="Kasabian",
    picture="https://www.inmusicfestival.com/sites/default/files/styles/large/public/inm-web-800x600-kasabian.jpg?itok=DWnM_kEl",
    website="http://www.kasabian.co.uk/",
    info="Kasabian are an English rock band formed in Leicester in 1997.  The band's original members consisted of vocalist Tom Meighan, guitarist and vocalist Sergio Pizzorno, guitarist Chris Karloff, and bassist Chris Edwards. Their music has won them several awards and recognition in the media, including a Brit Award in 2010 for Best British Group.",
    genre="Rock")
    kill.save()
    kas.save()


    c=Event(name=kill, date="2018-05-18", venue=a)
    d=Event(name=kas, date="2018-05-25", venue=a)
    e=Event(name=kas, date="2018-06-07", venue=b)
    f=Event(name=kill, date="2018-06-08", venue=b)
    c.save()
    
    d.save()
    e.save()
    f.save()

    

    
if __name__=='__main__':
    print("populating")
    populate()
