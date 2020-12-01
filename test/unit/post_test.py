from unittest import TestCase
from post import Post

class PostTest(TestCase):

    def test_init(self):
        p = Post('Test', 'Test Content')
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    def test_repr(self):
        p = Post('Test', 'Test Content')
        self.assertEqual(str(p), "Title Test and content Test Content.")