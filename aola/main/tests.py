from rest_framework import status
from rest_framework.test import APITestCase

from .constants import FilterKeyWords
from .models import Achievement, Ad, UsersAchievements, Note, User


class TestFeedAPIView(APITestCase):
    URL = '/feed/{id}/'

    def test_notes(self):
        user1 = User.objects.create(name='name1', surname='surname1')
        user2 = User.objects.create(name='name2', surname='surname2')
        Note.objects.create(title='tn1', body='b', user=user1)
        Note.objects.create(title='tn2', body='b', user=user1)
        Note.objects.create(title='tn3', body='b', user=user2)
        url1 = self.URL.format(id=user1.pk)
        url2 = self.URL.format(id=user2.pk)

        response1 = self.client.get(url1)
        response2 = self.client.get(url2)

        self.assertEqual(status.HTTP_200_OK, response1.status_code)
        self.assertEqual(status.HTTP_200_OK, response2.status_code)
        self.assertEqual(response1.data[0]['content_type'], 'note')
        self.assertEqual(response2.data[0]['content_type'], 'note')
        self.assertEqual(len(response1.data), 2)
        self.assertEqual(len(response2.data), 1)

    def test_ad(self):
        user1 = User.objects.create(name='name1', surname='surname1')
        Ad.objects.create(title='tad1', description='td1', url='urlone.com')
        Ad.objects.create(title='tad2', description='td1', url='urlone.com')
        url1 = self.URL.format(id=user1.pk)

        response1 = self.client.get(url1)

        self.assertEqual(status.HTTP_200_OK, response1.status_code)
        self.assertEqual(response1.data[0]['content_type'], 'ad')
        self.assertEqual(len(response1.data), 2)

    def test_achievements(self):
        user1 = User.objects.create(name='name1', surname='surname1')
        user2 = User.objects.create(name='name2', surname='surname2')
        ach1 = Achievement.objects.create(title='ta1', reasons='tr1')
        ach2 = Achievement.objects.create(title='ta2', reasons='tr2')
        UsersAchievements.objects.create(user=user1, achievement=ach1)
        UsersAchievements.objects.create(user=user1, achievement=ach2)
        url1 = self.URL.format(id=user1.pk)
        url2 = self.URL.format(id=user2.pk)

        response1 = self.client.get(url1)
        response2 = self.client.get(url2)

        self.assertEqual(status.HTTP_200_OK, response1.status_code)
        self.assertEqual(status.HTTP_200_OK, response2.status_code)
        self.assertEqual(response1.data[0]['content_type'], 'achievement')
        self.assertEqual(len(response1.data), 2)
        self.assertEqual(len(response2.data), 0)

    def test_search(self):
        user1 = User.objects.create(name='name1', surname='surname1')
        ach1 = Achievement.objects.create(title='ta1', reasons='tr1')
        UsersAchievements.objects.create(user=user1, achievement=ach1)
        Ad.objects.create(title='tad1', description='td1', url='urlone.com')
        Note.objects.create(title='tn1', body='b', user=user1)
        url = self.URL.format(id=user1.pk)

        response_note = self.client.get(f"{url}?search=tn1")
        response_ach = self.client.get(f"{url}?search=ta1")

        self.assertEqual(status.HTTP_200_OK, response_note.status_code)
        self.assertEqual(status.HTTP_200_OK, response_ach.status_code)
        self.assertEqual(len(response_note.data), 2)
        self.assertEqual(response_note.data[0]['content_type'], 'ad')
        self.assertEqual(response_note.data[1]['content_type'], 'note')
        self.assertEqual(len(response_ach.data), 2)
        self.assertEqual(response_ach.data[0]['content_type'], 'ad')
        self.assertEqual(response_ach.data[1]['content_type'], 'achievement')

    def test_filter(self):
        user1 = User.objects.create(name='name1', surname='surname1')
        ach1 = Achievement.objects.create(title='ta1', reasons='tr1')
        UsersAchievements.objects.create(user=user1, achievement=ach1)
        Ad.objects.create(title='tad1', description='td1', url='urlone.com')
        Note.objects.create(title='tn1', body='b', user=user1)
        url = self.URL.format(id=user1.pk)

        response_note = self.client.get(f"{url}?filter={FilterKeyWords.NOTE}")
        response_ach = self.client.get(f"{url}?filter={FilterKeyWords.ACHIEVEMENT}")

        self.assertEqual(status.HTTP_200_OK, response_note.status_code)
        self.assertEqual(status.HTTP_200_OK, response_ach.status_code)
        self.assertEqual(len(response_note.data), 2)
        self.assertEqual(response_note.data[0]['content_type'], 'ad')
        self.assertEqual(response_note.data[1]['content_type'], 'note')
        self.assertEqual(len(response_ach.data), 2)
        self.assertEqual(response_ach.data[0]['content_type'], 'ad')
        self.assertEqual(response_ach.data[1]['content_type'], 'achievement')

    def test_pagination(self):
        user1 = User.objects.create(name='name1', surname='surname1')
        ach1 = Achievement.objects.create(title='ta1', reasons='tr1')
        ach2 = Achievement.objects.create(title='ta2', reasons='tr2')
        UsersAchievements.objects.create(user=user1, achievement=ach1)
        UsersAchievements.objects.create(user=user1, achievement=ach2)
        Ad.objects.create(title='tad1', description='td1', url='urlone.com')
        Ad.objects.create(title='tad2', description='td2', url='urlone.com')
        Note.objects.create(title='tn1', body='b', user=user1)
        Note.objects.create(title='tn2', body='b', user=user1)
        url = self.URL.format(id=user1.pk)

        response1 = self.client.get(url)
        response2 = self.client.get(f"{url}?offset=2")
        response3 = self.client.get(f"{url}?limit=10")

        self.assertEqual(status.HTTP_200_OK, response1.status_code)
        self.assertEqual(status.HTTP_200_OK, response2.status_code)
        self.assertEqual(status.HTTP_200_OK, response3.status_code)
        self.assertEqual(len(response1.data), 2)
        self.assertEqual(len(response2.data), 2)
        self.assertEqual(len(response3.data), 6)
