from glasuntu.models import VenuePage

def create_user():
    # Create a user
    from glasuntu.models import User, UserProfile
    user = User.objects.get_or_create(username="testuser", password="test1234",
                                    email="testuser@testuser.com")[0]
    user.set_password(user.password)
    user.save()

    # Create a user profile
    user_profile = UserProfile.objects.get_or_create(user=user)[0]
    user_profile.save()

    return user, user_profile


def create_venues():
    # List of venues
    venues = []

    # Create venue pages from 1 to 10
    for i in range(1, 11):
        ven = Category(name="Venue " + str(i))
        ven.save()
        venues.append(cat)

    return venues
