import pytest
from pytest_factoryboy import register

from .factories import UserFactory, AdFactory, AchievementFactory, NoteFactory, UsersPostsFactory
from ..constants import FilterKeyWords
from ..models import Achievement, Ad, Note

URL = '/feed/{id}/'
register(UserFactory, "user", name='name1', surname='surname1')


@pytest.mark.django_db
def test_notes(client, user_with_notes):
    url = URL.format(id=user_with_notes.pk)

    response = client.get(url)

    assert response.status_code == 200
    assert response.data[0]['post_type'] == Note.POST_TYPE
    assert len(response.data) == 2


@pytest.mark.django_db
def test_achievement(client, user_with_achievements):
    url = URL.format(id=user_with_achievements.pk)

    response = client.get(url)

    assert response.status_code == 200
    assert response.data[0]['post_type'] == Achievement.POST_TYPE
    assert len(response.data) == 2


@pytest.mark.django_db
def test_ad(client, user, ad_1, ad_2):
    url = URL.format(id=user.pk)

    response = client.get(url)

    assert response.status_code == 200
    assert response.data[0]['post_type'] == Ad.POST_TYPE
    assert len(response.data) == 1


@pytest.mark.django_db
@pytest.mark.parametrize(
    ('search_param', 'search_result'),
    [
        pytest.param('tn1', 'tn1'),
        pytest.param('a1', 'a1')
    ])
def test_search(search_param, search_result, client, user, create_note, create_users_posts):
    create_users_posts(users=user, posts=create_note(title=search_param))
    create_users_posts(users=user, posts=create_note(title="title"))
    url = URL.format(id=user.pk)

    response = client.get(url, data={'search': search_param})

    assert response.status_code == 200
    assert response.data[0]['title'] == search_result
    assert len(response.data) == 1


@pytest.mark.django_db
@pytest.mark.parametrize(('filter_param'), [
    pytest.param(FilterKeyWords.NOTE),
    pytest.param(FilterKeyWords.ACHIEVEMENT),
])
def test_filter(filter_param, client, user_with_notes_and_achievements):
    url = URL.format(id=user_with_notes_and_achievements.pk)

    response = client.get(url, data={'filter': filter_param})

    assert response.status_code == 200
    for i in range(len(response.data)):
        assert response.data[i]['post_type'] == filter_param


@pytest.mark.django_db
def test_filter_error(client, user_with_notes_and_achievements):
    url = URL.format(id=user_with_notes_and_achievements.pk)

    response = client.get(url, data={'filter': "wrong_param"})

    assert response.status_code == 400


@pytest.mark.django_db
@pytest.mark.parametrize(('limit', 'offset', 'data_len'), [
    pytest.param(1, 0, 1),
    pytest.param(1, 0, 1),
    pytest.param(5, 0, 5),
    pytest.param(2, 1, 2),
])
def test_pagination(limit, offset, data_len, client, user_with_notes_and_achievements):
    url = URL.format(id=user_with_notes_and_achievements.pk)

    response = client.get(url, data={'limit': limit, 'offset': offset})

    assert response.status_code == 200
    assert len(response.data) == data_len
