from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class TestViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_authenticated_access(self):
        # Create a user
        user = User.objects.create_user('testuser', 'test@example.com', 'password')

        # Obtain a JWT token
        token_url = '/api/token/'
        token_response = self.client.post(token_url, data={'username': 'testuser', 'password': 'password'})
        token = token_response.data['access']

        # Set the JWT token in the request headers
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Make a request to the TestView
        response = self.client.get('/user/test-auth/')

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_access(self):
        # Make a request to the TestView without a JWT token
        response = self.client.get('/user/test-auth/')

        # Assert that the response status code is 403
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)