from django.test import TestCase
from .forms import ThingForm


# Create your tests here.

class ThingFormTestCase(TestCase):
    
    def setUp(self):
        self.form_input = {
            'name' : 'John',
            'description' : 'This is description',
            'quantity' : 3
        }  

    def form_has_necessary_fields(self):
        form = ThingForm()
        self.assertIn(name,form.fields)
        self.assertIn(description,form.fields)
        self.assertIn(quantity,form.fields)

    def form_accepts_valid_data(self):
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid)