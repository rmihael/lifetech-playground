import factory


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence('user-{0}'.format)
    email = factory.Sequence('user-{0}@example.com'.format)
    password = factory.PostGenerationMethodCall('set_password', 'password')

    class Meta:
        model = 'users.User'
        django_get_or_create = ('username', )
