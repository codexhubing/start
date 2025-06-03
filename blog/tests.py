from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class PostModelTest(TestCase):
    def test_create_post(self):
        user = User.objects.create_user("u", "u@example.com", "pass")
        post = Post.objects.create(author=user, title="Test", content="Content")
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(post.likes, 0)

    def test_like_once(self):
        user = User.objects.create_user("u", "u@example.com", "pass")
        post = Post.objects.create(author=user, title="Test", content="Content")
        post.liked_by.add(user)
        post.liked_by.add(user)
        self.assertEqual(post.likes, 1)
