# Blog-Django-4.2.3-DjangoRestFramework-3.14.0-And-Vue-3.3.4

## Description

This repository is a Software of Application with Python.

## Virtual

Using pipenv, virtualenv preferably.

## Installation

Using Django 4.2.3, Django Rest Framework 3.14.0 preferably.

![alt text](https://i.ytimg.com/vi/7GWKv03Osek/maxresdefault.jpg)

## DataBase

Using SQLite3, PostgreSQL, MySQL, MongoDB,etc.

## Apps

Using Postman, Insomnia, Talend API Tester,etc.



## Usage

```shell
$ git clone https://github.com/DanielArturoAlejoAlvarez/Blog-Django-4.2.3-DjangoRestFramework-3.14.0-And-Vue-3.3.4.git

```

Follow the following steps and you're good to go! Important:

![alt text](https://taswar.zeytinsoft.com/wp-content/uploads/2016/11/djangoProjectCodDjango.gif)

## Coding

### Config

```python
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

### Routes

```python
# admin
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls',namespace='blog')),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# blog
from django.urls import path

from .views import BlogListView, DetailPostView

app_name='blog'

urlpatterns = [
    path('posts/', BlogListView.as_view()),
    path('posts/<post_slug>', DetailPostView.as_view()),
]
```

### Models

```python
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
    
```

### Views

```python
from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class BlogListView(APIView):
    def get(self,request,*args,**kwargs):
        posts=Post.postobjects.all()[0:4]

        serializer=PostSerializer(posts, many=True)#FIXME: using many posts reference

        return Response(serializer.data)
    
class DetailPostView(APIView):
    def get(self,request,post_slug,*args,**kwargs):
        post=get_object_or_404(Post, slug=post_slug)#FIXME: func get_object_or_404 return Obj or HttpException 404 
        serializer=PostSerializer(post)  

        return Response(serializer.data)      
```

### Serializers

```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
        class Meta:
                model=Post
                fields=(
                        'id',
                        'title',
                        'thumbnail',
                        'excerpt',
                        'content',
                        'slug',
                        'published',
                        'author',
                        'status',                        
                )
```

### Frontend
```html
<template>
  <div class="relative py-16 overflow-hidden">
    <div class="relative px-4 sm:px-6 lg:px-8">
      <div class="max-w-2xl text-lg mx-auto shadow-lg p-2">
        <div class="flex bg-red-700 text-white text-xl">
          <img
            class="mr-2"
            width="28"
            src="../assets//img/time-and-calendar.png"
          />{{ getDateTime(this.post.published) }}
        </div>
        <img :src="base + this.post.thumbnail" />

        <h1>
          <span
            class="mt-2 block text-3xl text-center leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl"
            >{{ this.post.title }}</span
          >
        </h1>
        <p class="mt-8 text-2xl font-bold text-gray-700 leading-8">
          {{ this.post.excerpt }}
        </p>

        <div class="mt-6 prose prose-indigo prose-lg text-gray-500 mx-auto">
          {{ this.post.content }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HelloWorld from "@/components/HelloWorld.vue";
import { getAPI } from "../assets/js/api.js";


export default {
  name: "PostDetailView",
  components: {
    HelloWorld,
  },
  data() {
    return {
      post: {},
      base: getAPI.defaults.baseURL
    };
  },
  methods: {
   getDateTime(dt){
    let date = new Date(dt).toDateString()
    let time = new Date(dt).toLocaleTimeString()
    
    return date+' '+time
   }
  },
  created() { 
    getAPI
      .get(`/blog/posts/${this.$route.params.slug}`)
      .then((res) => {
        this.post = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/DanielArturoAlejoAlvarez/Blog-Django-4.2.3-DjangoRestFramework-3.14.0-And-Vue-3.3.4. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

```

```