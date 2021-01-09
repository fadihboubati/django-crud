from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Menu

# Create your tests here.
class Food_Project_test(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'Mohammad',
            email = 'mohammad@gmail.com',
            password = 'mhd123456'
        )
        self.menu = Menu.objects.create(
            user = self.user,
            name = 'Big Rami',
            fav_drink = 'whey protein',
            fav_meal = 'chicken',
            eating_frequency_per_day = '10',
            like_spicy = False
        )

    def test_snacks_page_status(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_snack_details_status(self):
        response = self.client.get(reverse('dish_details', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_snack_details_content(self):
        response = self.client.get(reverse('dish_details', args='1'))
        self.assertContains(response, 'Big Rami')

    def test_snack_update(self):
        response = self.client.post(reverse('update_view', args='1'), {
            'fav_meal': 'Fish',
        })
        self.assertContains(response, 'Fish')
        self.assertNotContains(response, 'salad')
