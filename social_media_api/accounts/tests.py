from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post

class FollowTests(APITestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(username='user1', password='password')
        self.user2 = get_user_model().objects.create_user(username='user2', password='password')
        self.client.login(username='user1', password='password')

    def test_follow_user(self):
        response = self.client.post(f'/follow/{self.user2.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user2, self.user1.following.all())

    def test_feed(self):
        Post.objects.create(author=self.user2, title='Test Post', content='This is a test post')
        response = self.client.get('/feed/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Post', str(response.data))