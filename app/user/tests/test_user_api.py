from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create_user')
CREAT_COLLECTOR_URL = reverse('user:create_collector')
CREATE_SELLER_URL = reverse('user:create_seller')




user_reg = {
    'email':'user@example.com',
    'password':'123password',
    'name':'user one'
}

user_collector = {
    'email':'collector@example.com',
    'password':'123password',
    'name':'collector one',
    'is_collector': True,
}

user_seller = {
    'email':'seller@example.com',
    'password':'123password',
    'name':'Seller One',
    'is_collector': True,
    'is_seller': True,
}

class PublicApiTests(TestCase):

    # Test to Create a Regualr User
    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        res = self.client.post(CREATE_USER_URL, user_reg)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=user_reg['email'])
        self.assertNotIn('password', res.data)

    def test_user_rasies_error_with_dupicalte_emails(self):
        get_user_model().objects.create(**user_reg)
        res = self.client.post(CREATE_USER_URL, user_reg)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_password_length(self):
        user_reg['password'] = 'pw'
        res = self.client.post(CREATE_USER_URL, user_reg)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(email=user_reg['email']).exists()
        self.assertFalse(user_exists)

    def test_create_collector_succes(self):
        res = self.client.post(CREAT_COLLECTOR_URL, user_collector)
        collector = get_user_model().objects.get(email=user_collector['email'])

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(collector.is_collector)
        self.assertFalse(collector.is_seller)

    def test_create_seller_success(self):
        res = self.client.post(CREATE_SELLER_URL, user_seller)
        seller = get_user_model().objects.get(email=user_seller['email'])

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(seller.is_collector)
        self.assertTrue(seller.is_seller)
