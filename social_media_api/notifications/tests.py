# Example test
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Like

User = get_user_model()

class LikePostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(title='Test Post', content='Test Content')

    def test_like_post(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(f'/posts/{self.post.id}/like/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Like.objects.filter(user=self.user, post=self.post).exists())