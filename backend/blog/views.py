from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class BlogListView(APIView):
    def get(self,request,*args,**kwargs):
        posts=Post.postobjects.all()[0:4]

        serializer=PostSerializer(posts, many=True)

        return Response(serializer.data)