from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Posts
# Create your tests here.


class dockerTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username='testuser', password='password')
        testuser1.save()

        testpost = Posts.objects.create(
            author=testuser1,
            title='booktitletest',
            isbn='1234567891234',
            released='8/01/2018',
        )

        testpost.save()

    def test_post_content(self):
        post = Posts.objects.get(id=1)
        act_auth = str(post.author)
        act_title = str(post.title)
        act_isbn = str(post.isbn)
        act_rel = str(post.released)

        self.assertEqual(act_auth, 'testuser1')
        self.assertEqual(act_title, 'booktitletest')
        self.assertEqual(act_isbn, '1234567891234')
        self.assertEqual(act_rel, '8/01/2018')
