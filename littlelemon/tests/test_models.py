from django.test import TestCase
from restaurant.models import Booking, MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='Test Item', price=10.0000, inventory=10)
        itemstr = item.get_item()

        self.assertEqual(itemstr, 'Test Item : 10.00')
