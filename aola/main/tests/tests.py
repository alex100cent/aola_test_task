import pytest
from pytest_factoryboy import register

from .factories import UserFactory, AdFactory, AchievementFactory, NoteFactory, UsersPostsFactory
from ..constants import FilterKeyWords
from ..models import Achievement, Ad, Note

URL = '/feed/{id}/'
register(UserFactory, "user", name='name1', surname='surname1')


@pytest.mark.django_db
def test_notes(client, user):
    n1 = NoteFactory()
    n2 = NoteFactory()
    UsersPostsFactory(users=user, posts=n1)
    UsersPostsFactory(users=user, posts=n2)
    url = URL.format(id=user.pk)

    response = client.get(url)

    assert response.status_code == 200
    assert response.data[0]['post_type'] == Note.POST_TYPE
    assert len(response.data) == 2


@pytest.mark.django_db
def test_achievement(client, user):
    a1 = AchievementFactory(title='a1', body='b')
    a2 = AchievementFactory(title='a2', body='b')
    UsersPostsFactory(users=user, posts=a1)
    UsersPostsFactory(users=user, posts=a2)
    url = URL.format(id=user.pk)

    response = client.get(url)

    assert response.status_code == 200
    assert response.data[0]['post_type'] == Achievement.POST_TYPE
    assert len(response.data) == 2


@pytest.mark.django_db
def test_ad(client, user):
    AdFactory(title='ad1', body='b', url='test.url')
    url = URL.format(id=user.pk)

    response = client.get(url)

    assert response.status_code == 200
    assert response.data[0]['post_type'] == Ad.POST_TYPE


@pytest.mark.django_db
@pytest.mark.parametrize(
    ('search_param', 'search_result'),
    [
        pytest.param('tn1', 'tn1'),
        pytest.param('a1', 'a1')
    ])
def test_search(search_param, search_result, client, user):
    n1 = NoteFactory(title='tn1', body='b')
    a1 = AchievementFactory(title='a1', body='b')
    UsersPostsFactory(users=user, posts=n1)
    UsersPostsFactory(users=user, posts=a1)
    url = URL.format(id=user.pk)

    response = client.get(url, data={'search': search_param})

    assert response.status_code == 200
    assert response.data[0]['title'] == search_result


@pytest.mark.django_db
@pytest.mark.parametrize(('filter_param'), [
    pytest.param(FilterKeyWords.NOTE),
    pytest.param(FilterKeyWords.ACHIEVEMENT),
])
def test_filter(filter_param, client, user):
    for _ in range(3):
        note = NoteFactory(title='tn', body='b')
        achievement = AchievementFactory(title='a', body='b')
        UsersPostsFactory(users=user, posts=note)
        UsersPostsFactory(users=user, posts=achievement)
    url = URL.format(id=user.pk)

    response = client.get(url, data={'filter': filter_param})

    assert response.status_code == 200
    for i in range(len(response.data)):
        assert response.data[i]['post_type'] == filter_param


@pytest.mark.django_db
def test_filter_error(client, user):
    for _ in range(3):
        note = NoteFactory(title='tn', body='b')
        achievement = AchievementFactory(title='a', body='b')
        UsersPostsFactory(users=user, posts=note)
        UsersPostsFactory(users=user, posts=achievement)
    url = URL.format(id=user.pk)

    response = client.get(url, data={'filter': "wrong_param"})

    assert response.status_code == 400


@pytest.mark.django_db
@pytest.mark.parametrize(('limit', 'offset', 'data_len'), [
    pytest.param(1, 0, 1),
    pytest.param(1, 0, 1),
    pytest.param(5, 0, 5),
    pytest.param(2, 1, 2),
])
def test_pagination(limit, offset, data_len, client, user):
    for _ in range(3):
        note = NoteFactory(title='tn', body='b')
        achievement = AchievementFactory(title='a', body='b')
        UsersPostsFactory(users=user, posts=note)
        UsersPostsFactory(users=user, posts=achievement)
    url = URL.format(id=user.pk)

    response = client.get(url, data={'limit': limit, 'offset': offset})

    assert response.status_code == 200
    assert len(response.data) == data_len
