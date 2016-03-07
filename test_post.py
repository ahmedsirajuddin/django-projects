from django.test import TestCase

# Create your tests here.

# Importing this from the DRF example of APIClient unittesting.
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from CMSApp.models import Post

class PostTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='a', password='a', email='a@hotmail.com')
        User.objects.create_user(username='b', password='b', email='b@hotmail.com')

    def test_create_post(self):
        """
        Ensure authenticated users can create a new post object.
        """
        url = reverse('post-list')

        data = {'post': 'Test post.'}

        # See if unauthenicated users can create a post (they shouldn't).
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # See if authenicated users can create a post (they should).
        self.client.login(username='a', password='a')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.get().owner.username, 'a')
        self.assertEqual(Post.objects.get().post, 'Test post.')


    def test_get_post_list(self):
        """
        Ensure no one can get a list of all post objects.
        """
        url = reverse('post-list')

        # See if unauthenticated users can get a list of spill (they shouldn't.)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # See if authenticated users can get a list of post (they shouldn't).
        self.client.login(username='a', password='a')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # See if authenticated admins can get a list of post (they shouldn't).
        User.objects.create_superuser(username='c', password='c', email='c@hotmail.com')
        self.client.login(username='c', password='c')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_post_detail(self):
        """
        Ensure only authenticated users can access the detail of the post.
        """
        Post.objects.create(post='test', owner=User.objects.get(username='a'))
        url = reverse('post-detail', kwargs={'pk':1})

        # See if unauthenticated users can get a post object (they shouldn't.)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # See if authenticated users can get a post object (they should).
        self.client.login(username='b', password='b')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # See if authenticated admins can get a post object (they should).
        User.objects.create_superuser(username='c', password='c', email='c@hotmail.com')
        self.client.login(username='c', password='c')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_patch_post_detail(self):
        """
        Ensure no one can patch a post object.
        """
        Post.objects.create(post='test', owner=User.objects.get(username='a'))
        url = reverse('post-detail', kwargs={'pk':1})

        # See if unauthenticated users can patch a post object (they shouldn't.)
        response = self.client.patch(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # See if authenticated users can patch a post object (not owner) (they shouldn't).
        self.client.login(username='b', password='b')
        response = self.client.patch(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # See if authenticated owners can patch a post object (they shouldn't).
        self.client.login(username='a', password='a')
        response = self.client.patch(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # See if authenticated admins can patch a post object (they shouldn't).
        User.objects.create_superuser(username='c', password='c', email='c@hotmail.com')
        self.client.login(username='c', password='c')
        response = self.client.patch(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_post_detail(self):
        """
        Ensure no one can put a post object.
        """
        Post.objects.create(post='test', owner=User.objects.get(username='a'))
        url = reverse('post-detail', kwargs={'pk':1})

        # See if unauthenticated users can put a post object (they shouldn't.)
        response = self.client.put(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # See if authenticated users can put a post object (not owner) (they shouldn't).
        self.client.login(username='b', password='b')
        response = self.client.put(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # See if authenticated owners can put a post object (they shouldn't).
        self.client.login(username='a', password='a')
        response = self.client.put(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # See if authenticated admins can put a post object (they shouldn't).
        User.objects.create_superuser(username='c', password='c', email='c@hotmail.com')
        self.client.login(username='c', password='c')
        response = self.client.put(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_post_detail(self):
        """
        Ensure only owners can delete a post object.
        """
        Post.objects.create(post='test', owner=User.objects.get(username='a'))
        url = reverse('post-detail', kwargs={'pk':1})

        # See if unauthenticated users can delete a post object (they shouldn't.)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # See if authenticated users can delete a post object (not owner) (they shouldn't).
        self.client.login(username='b', password='b')
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # See if authenticated owners can delete a post object (not owner) (they should).
        self.client.login(username='a', password='a')
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Recreate the post because it was sucessfully deleted above.
        Post.objects.create(post='test', owner=User.objects.get(username='a'))
        url = reverse('post-detail', kwargs={'pk':2})

        # See if authenticated admins can delete a post object (they should).
        User.objects.create_superuser(username='c', password='c', email='c@hotmail.com')
        self.client.login(username='c', password='c')
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_like_post(self):
        """
        Ensure only authenticated users can like the object.
        """
        Post.objects.create(post='test', owner=User.objects.get(username='a'))
        url = reverse('post-like', kwargs={'pk':1})

        # See if unauthenticated users can like a post object (they shouldn't.)
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # See if authenticated users can like a post object (not owner) (they should).
        self.client.login(username='b', password='b')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.get().usersVoted.count(), 1)
        self.assertEqual(Post.objects.get().usersVoted.get().username, 'b')

        # See if authenticated owners can like the post object (they should).
        self.client.login(username='a', password='a')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.get().usersVoted.count(), 2)

    def test_unlike_post(self):
        """
        Ensure only authenticated users can unlike the object.
        """
        Post.objects.create(post='test', owner=User.objects.get(username='a'))
        Post.objects.get().usersVoted.add(User.objects.get(username='b'))
        url = reverse('post-unlike', kwargs={'pk':1})

        # See if unauthenticated users can unlike a post object (they shouldn't.)
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # See if authenticated users can unlike a post object (they should).
        self.assertEqual(Post.objects.get().usersVoted.count(), 1)
        self.assertEqual(Post.objects.get().usersVoted.get().username, 'b')
        self.client.login(username='b', password='b')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.get().usersVoted.count(), 0)

        # See if authenticated owners can unlike the post object (they should).
        Post.objects.get().usersVoted.add(User.objects.get(username='a'))
        self.assertEqual(Post.objects.get().usersVoted.count(), 1)
        self.assertEqual(Post.objects.get().usersVoted.get().username, 'a')

        self.client.login(username='a', password='a')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.get().usersVoted.count(), 0)
