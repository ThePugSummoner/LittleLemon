from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
#from restaurant.views import MenuItemsView
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    
    def setUp(self):
        Menu.objects.create(title="Tomato Soup", price = 9.90, inventory = 4)
        Menu.objects.create(title="Pasta Bolognese", price = 13.90, inventory = 6)

        self.client = APIClient()

    def test_getall(self):
        url = reverse('menu')
        response = self.client.get(url)
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        print("Response Data:", response.data)
        print("Serializer Data:", serializer.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'], serializer.data)