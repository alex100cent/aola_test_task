import pytest

from ..constants import FilterKeyWords
from ..models import Achievement, Ad, UsersPosts, Note, User

URL = '/feed/{id}/'


@pytest.mark.django_db
def test_notes(client):
    user = User.objects.create(name='name1', surname='surname1')
    n1 = Note.objects.create(title='tn1', body='b')
    n2 = Note.objects.create(title='tn2', body='b')
    UsersPosts.objects.create(users=user, posts=n1)
    UsersPosts.objects.create(users=user, posts=n2)
    url = URL.format(id=user.pk)

    response = client.get(url)

    assert response.status_code == 200
    assert response.data[0]['post_type'] == 'note'
    assert len(response.data) == 2


@pytest.mark.django_db
def test_achievement(client):
    user = User.objects.create(name='name1', surname='surname1')
    a1 = Achievement.objects.create(title='a1', body='b')
    a2 = Achievement.objects.create(title='a2', body='b')
    UsersPosts.objects.create(users=user, posts=a1)
    UsersPosts.objects.create(users=user, posts=a2)
    url = URL.format(id=user.pk)

    response = client.get(url)

    assert response.status_code == 200
    assert response.data[0]['post_type'] == 'achievement'
    assert len(response.data) == 2


@pytest.mark.django_db
def test_ad(client):
    user = User.objects.create(name='name1', surname='surname1')
    Ad.objects.create(title='ad1', body='b', url='test.url')
    url = URL.format(id=user.pk)

    response = client.get(url)

    assert response.status_code == 200
    assert response.data[0]['post_type'] == 'ad'


@pytest.mark.django_db
@pytest.mark.parametrize(
    ('search_param', 'search_result'),
    [
        pytest.param('tn1', 'tn1'),
        pytest.param('a1', 'a1')
    ])
def test_search(search_param, search_result, client):
    user = User.objects.create(name='name1', surname='surname1')
    n1 = Note.objects.create(title='tn1', body='b')
    a1 = Achievement.objects.create(title='a1', body='b')
    UsersPosts.objects.create(users=user, posts=n1)
    UsersPosts.objects.create(users=user, posts=a1)
    url = URL.format(id=user.pk)

    response = client.get(url, data={'search': search_param})

    assert response.status_code == 200
    assert response.data[0]['title'] == search_result


@pytest.mark.django_db
@pytest.mark.parametrize(('filter_param'), [
    pytest.param(FilterKeyWords.NOTE),
    pytest.param(FilterKeyWords.ACHIEVEMENT),
])
def test_filter(filter_param, client):
    user = User.objects.create(name='name1', surname='surname1')
    for _ in range(3):
        note = Note.objects.create(title='tn', body='b')
        achievement = Achievement.objects.create(title='a', body='b')
        UsersPosts.objects.create(users=user, posts=note)
        UsersPosts.objects.create(users=user, posts=achievement)
    url = URL.format(id=user.pk)

    response = client.get(url, data={'filter': filter_param})

    assert response.status_code == 200
    for i in range(len(response.data)):
        assert response.data[i]['post_type'] == filter_param


@pytest.mark.django_db
def test_filter_error(client):
    user = User.objects.create(name='name1', surname='surname1')
    for _ in range(3):
        note = Note.objects.create(title='tn', body='b')
        achievement = Achievement.objects.create(title='a', body='b')
        UsersPosts.objects.create(users=user, posts=note)
        UsersPosts.objects.create(users=user, posts=achievement)
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
def test_pagination(limit, offset, data_len, client):
    user = User.objects.create(name='name1', surname='surname1')
    for _ in range(3):
        note = Note.objects.create(title='tn', body='b')
        achievement = Achievement.objects.create(title='a', body='b')
        UsersPosts.objects.create(users=user, posts=note)
        UsersPosts.objects.create(users=user, posts=achievement)
    url = URL.format(id=user.pk)

    response = client.get(url, data={'limit': limit, 'offset': offset})

    assert response.status_code == 200
    assert len(response.data) == data_len
