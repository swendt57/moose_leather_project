from django.test import TestCase
from django.core.management import call_command
from .models import Item, Category


class TestProductModels(TestCase):

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

    def test_get_retail_page(self):
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "retail_items.html")

    # TODO NOT WORKING!!
    # def test_get_consignment_page(self):
    #     page = self.client.get("/products/consigned/")
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "consigned_items.html")

    # def test_render_consigned_item_upload_page(self):
    #     page = self.client.get("/products/upload_consigned")
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "upload_consigned_item.html")
