from django.test import TestCase
from .forms import ThingForm

# Create your tests here.

class ThingFormTestCase(TestCase):
    
    def test_valid_sign_up_form(self):
        self.form_input = {
            'name' : 'Jaeho',
            'description' : 'This is Jaeho signing up',
            'quantity' : '3'
        }
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())
        self.assertFalse(form.is_invalid())