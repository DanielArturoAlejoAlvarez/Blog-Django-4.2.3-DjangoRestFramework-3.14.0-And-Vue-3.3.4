from django.db import models
from django.db.models.query import QuerySet

from django.utils import timezone
from django.contrib.auth.models import User


def user_directory_path(instance,filename):
    return 'blog/{0}/{1}'.format(instance.title, filename)


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft','Draft'),
        ('published','Published'),
    )

    title=models.CharField(max_length=250)
    thumbnail=models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    excerpt=models.TextField(null=True)
    content=models.TextField()
    slug=models.SlugField(max_length=250, unique_for_date='published', null=False, unique=True)
    published=models.DateTimeField(default=timezone.now)

    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    status=models.CharField(max_length=10, choices=options, default='draft')

    objects=models.Manager()
    postobjects=PostObjects()

    class Meta:
        ordering=('-published',)        

    def __str__(self):
        return self.title
    
    