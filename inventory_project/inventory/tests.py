from django.contrib.staticfiles.testing import LiveServerTestCase
from django.urls import reverse
from django.conf import settings
from selenium import webdriver
from inventory.models import Inventory, Supplier

class InventoryPageTests(LiveServerTestCase):

    def setUp(self):
        settings.TEST_SERVER_URL = self.live_server_url
        self.supplier = Supplier.objects.create(name="Test Supplier")
        self.inventory = Inventory.objects.create(
            name="Test Item",
            description="Test Description",
            stock=10,
            availability=True,
            supplier=self.supplier
        )

    def test_inventory_list_page(self):
        response = self.client.get(self.live_server_url + reverse("inventory-list"))
        self.assertEqual(response.status_code, 200)

    def test_api_inventory_page(self):
        response = self.client.get(self.live_server_url + "/api/inventory/")
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail_page(self):
        response = self.client.get(self.live_server_url + reverse("inventory-detail", args=[self.inventory.id]))
        self.assertEqual(response.status_code, 200)
