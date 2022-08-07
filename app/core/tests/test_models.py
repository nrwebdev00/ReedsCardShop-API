# Test for Modles

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):

        email = 'test@example.com'
        password = '98eTi5!Ob4rX'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_email = [
            ['test1@example.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, excepted in sample_email:
            user = get_user_model().objects.create_user(email, '98eTi5!Ob4rX')
            self.assertEqual(user.email, excepted)

    def test_new_user_without_email_rasies_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', '98eTi5!Ob4rX')

    # Create Users Test - user, collector, seller, superuser
    def test_new_user_collector(self):
        user = get_user_model().objects.create_user_collector(
            'test@example.com',
            '98eTi5!Ob4rX',
        )

        self.assertTrue(user.is_collector)

    def test_new_user_seller(self):
        user = get_user_model().objects.create_user_seller(
            'test@example.com',
            '98eTi5!Ob4rX',
        )

        self.assertTrue(user.is_collector)
        self.assertTrue(user.is_seller)

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            '98eTi5!Ob4rX',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_collector)
        self.assertTrue(user.is_seller)

    # Change User Boolean Fields

    def test_change_user_collector(self):
        email = 'test@example.com'
        user = get_user_model().objects.create_user(
            email,
            '98eTi5!Ob4rX',
        )
        user = get_user_model().objects.change_user_collector(email)

        self.assertTrue(user.is_collector)

    def test_change_user_seller(self):
        email = 'test@example.com'
        user = get_user_model().objects.create_user(
            email,
            '98eTi5!Ob4rX',
        )
        user = get_user_model().objects.change_user_seller(email)

        self.assertTrue(user.is_seller)
        self.assertTrue(user.is_collector)
