from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_create_post(self):
        post = Post.objects.create(title="Test", content="Content")
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(post.likes, 0)
