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
