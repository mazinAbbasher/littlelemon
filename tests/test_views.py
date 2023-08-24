from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)
        Menu.objects.create(title="Burger", price=60, inventory=200)



    def test_getall(self):

        url = reverse('bb')
        response = self.client.get(url)
        data = Menu.objects.all()
        serializer = MenuSerializer(data,many=True)
        expected_data = serializer.data


        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)