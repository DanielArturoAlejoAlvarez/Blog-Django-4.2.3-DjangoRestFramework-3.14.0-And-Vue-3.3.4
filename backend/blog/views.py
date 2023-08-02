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