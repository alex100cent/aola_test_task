import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'main.User'

    name = factory.Faker('first_name')
    surname = factory.Faker('last_name')


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'main.Ad'


class AchievementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'main.Achievement'


class NoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'main.Note'


class UsersPostsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'main.UsersPosts'
