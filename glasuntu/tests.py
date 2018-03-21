from django.test import TestCase
from django.conf import settings
import os.path
from django.core.urlresolvers import reverse
from glasuntu import views
# Create your tests here.
class Tests(TestCase):

    def test_base_template_exists(self):
        # Check base.html exists inside template folder
        path_to_base = settings.BASE_DIR + '/glasuntu/templates/glasuntu/base.html'
        print(path_to_base)
        self.assertTrue(os.path.isfile(path_to_base))



class ModelTests(TestCase):

    def setUp(self):
        try:
            from populate import populate
            populate()
        except ImportError:
            print('The module populate does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')
        
        
    def get_venue(self, name):
        
        from glasuntu.models import VenuePage
        try:                  
            ven = VenuePage.objects.get(name=name)
        except VenuePage.DoesNotExist:    
            ven = None
        return ven

    #test that venue with name barrowland ballroom exists (in our populate script    
    def test_bb_ven_added(self):
        ven = self.get_venue('Barrowland Ballroom')  
        self.assertIsNotNone(ven)

     #test index page has a title    
    def test_view_has_title(self):
        response = self.client.get(reverse('glasuntu:index'))

        #Check title used correctly
        self.assertIn('<title>'.encode(), response.content)
        self.assertIn('</title>'.encode(), response.content)

#check that register/login appear when not logged in
    def test_url_reference_in_index_page_when_not_logged(self):
        #Access index page with user not logged
        response = self.client.get(reverse('glasuntu:index'))

        # Check links that appear for logged person only
        self.assertIn(reverse('glasuntu:register'), response.content.decode('ascii'))
        self.assertIn(reverse('glasuntu:login'), response.content.decode('ascii'))

