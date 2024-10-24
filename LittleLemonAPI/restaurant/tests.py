from django.test import TestCase
from .models import Menu
from rest_framework.test import APIClient
from .serializers import MenuItemSerializer
from django.http import HttpResponse
from django.contrib.auth.models import User

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title = 'IceCream', price = 80)
        self.assertEqual(str(item), "IceCream : 80")   



class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.menu_items = [
            Menu.objects.create(title = 'Yogurt', price =3.50, inventory=8),
            Menu.objects.create(title ='Pizza', price=10.50, inventory=12),
            Menu.objects.create(title='Lamb', price=20.66, inventory=8),
        ]

    def test_getall(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/restaurant/menu/')
        serializer = MenuItemSerializer(self.menu_items, many =True)
        self.assertEqual(response.data, serializer.data)