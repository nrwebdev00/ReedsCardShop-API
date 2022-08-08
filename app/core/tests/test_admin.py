# Test for django admin pannel

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='98eTi5!Ob4rX'
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='98eTi5!Ob4rX',
            name='Test User',
        )

        self.user_collector = get_user_model().objects.create_user_collector(
            email='collector@example.com',
            password="98eTi5!Ob4rX",
            name='Collector User',
        )

        self.user_seller = get_user_model().objects.create_user_seller(
            email='seller@gmail.com',
            password='98eTi5!Ob4rX',
            name='Seller User'
        )

    def test_user_list_admin_pannel(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)