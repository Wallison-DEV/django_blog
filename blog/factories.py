import factory
from blog.models import Post 
from faker import Factory as FakerFactory

from django.contrib.auth.models import User
from django.utils.timezone import now

faker = FakerFactory.create()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        
    email = factory.LazyAttribute(lambda x: faker.safe_email())  # Corrigido aqui
    username = factory.LazyAttribute(lambda x: faker.name())
    
    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create: 
                user.save()
        return user
    
class PostFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.sentence())
    created_on = factory.LazyAttribute(lambda x: now())  # Corrigido aqui
    author = factory.SubFactory(UserFactory)
    status = 0
    
    class Meta:
        model = Post
