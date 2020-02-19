from django.test import TestCase
from .forms import User, UserRegistrationForm

class TestAccountForms(TestCase):
    """Test all forms used in the Accounts app"""

    # TODO Have to do research as to how to test authentication stuff
    
    # def test_passwords_must_match(self):
    #     form = UserRegistrationForm({
    #         'first_name': 'John',
    #         'last_name': 'Doe',
    #         'email': 'someone@anything.com',
    #         'username': 'jdoe',
    #         'password1': 'anything',
    #         'password2': 'anything'
    #     })
    #     form.clean_email()
    #     form.clean_password2()
    #     print(form.is_valid())
    #     self.assertTrue(form.is_valid())
