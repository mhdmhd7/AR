from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, PasswordReset
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.authtoken.models import Token

class SignUpLoginTests(APITestCase):
    def test_login_failure(self):
        url = reverse('login')
        data = {
            'username': 'nonexistent_user',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_success(self):
        # First, create a test user
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

        # Then, attempt to login with the created user
        url = reverse('login')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
