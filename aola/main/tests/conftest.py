import pytest

from .factories import UserFactory, AdFactory, AchievementFactory, NoteFactory, UsersPostsFactory


@pytest.fixture
def create_note():
    return NoteFactory


@pytest.fixture
def create_users_posts():
    return UsersPostsFactory


@pytest.fixture
def user() -> UserFactory:
    return UserFactory()


@pytest.fixture
def note_1() -> NoteFactory:
    return NoteFactory(title="note 1", body="this is body")


@pytest.fixture
def note_2() -> NoteFactory:
    return NoteFactory(title="note 2", body="this is body")


@pytest.fixture
def ad_1() -> AdFactory:
    return AdFactory(title="ad 1", body="this is body", url="url.com")


@pytest.fixture
def ad_2() -> AdFactory:
    return AdFactory(title="ad 2", body="this is body", url="url.com")


@pytest.fixture
def achievement_1() -> AchievementFactory:
    return AchievementFactory(title="ach 1")


@pytest.fixture
def achievement_2() -> AchievementFactory:
    return AchievementFactory(title="ach 2")


@pytest.fixture
def user_with_notes(note_1, note_2) -> UserFactory:
    user = UserFactory()
    UsersPostsFactory(users=user, posts=note_1)
    UsersPostsFactory(users=user, posts=note_2)
    return user


@pytest.fixture()
def user_with_achievements(user, achievement_1, achievement_2) -> UserFactory:
    UsersPostsFactory(users=user, posts=achievement_1)
    UsersPostsFactory(users=user, posts=achievement_2)
    return user


@pytest.fixture()
def user_with_notes_and_achievements() -> UserFactory:
    user = UserFactory()
    for _ in range(3):
        UsersPostsFactory(users=user, posts=NoteFactory())
        UsersPostsFactory(users=user, posts=AchievementFactory())
    return user
