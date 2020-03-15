from django.test import TestCase, Client
from django.core.management import call_command
from django.shortcuts import reverse
from django.contrib.auth.models import User
from unittest.mock import patch
from .models import Item, Category


class TestProductModels(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'john@doe.com', 'secret')

    @classmethod
    def setUpClass(cls):
        # Be sure to add the call to super!
        super(TestProductModels, cls).setUpClass()
        call_command('loaddata', 'products.yaml', verbosity=0)

    def test_item_creation(self):
        # You MUST call XXX.objects.create within the test otherwise it tries to use non-test tables
        item = Item.objects.create(title="item_name", description="engaging description", price=50,
                                   category=Category.objects.get(id=2), is_consignment=False, image="a\\path")
        self.assertTrue(isinstance(item, Item))
        self.assertEqual(item.__str__(), item.title)

    def test_item_string_representation(self):
        item = Item(title='Create an Item')
        self.assertEqual(str(item), 'Create an Item')

    def test_category_string_representation(self):
        category = Category(name='Create a Category')
        self.assertEqual(str(category), 'Create a Category')


class TestProductViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    @patch('products.views.get_items_per_page')
    def test_get_retail_page(self, mock_get_items_per_page=3):
        page = self.client.get("/products/", mock_get_items_per_page)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "retail_items.html")

    @patch('products.views.get_items_per_page')
    def test_get_consignment_page(self, mock_get_items_per_page=3):
        page = self.client.get(reverse('consigned'), mock_get_items_per_page)  # why did I have to use "reverse" here to get it to work?
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "consigned_items.html")

    def test_render_consigned_item_upload_page(self):
        self.client.login(username='john', password='secret')
        page = self.client.get('/accounts/login/?next=/products/upload_consigned')
        self.assertEqual(page.status_code, 200)
        # self.assertTemplateUsed(page, "upload_consigned_item.html") -- unable to test for template in this case
