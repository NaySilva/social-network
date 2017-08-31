from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
import json
from posts.models import User, Post, Comment, Geo, Address
from posts.serializers import UserSerializer, PostSerializer, CommentSerializer, UserDetailSerializer, \
    PostDetailSerializer, AddressSerializer, GeoSerializer


class GeoList(generics.ListCreateAPIView):
    queryset = Geo.objects.all()
    serializer_class = GeoSerializer
    name = 'geo-list'

class GeoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Geo.objects.all()
    serializer_class = GeoSerializer
    name = 'geo-detail'

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-list'

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-detail'

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    name = 'user-detail'

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    name = 'post-detail'

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request):
        return Response({
            'user': reverse(UserList.name,
                               request=request),
            'comment': reverse(CommentList.name,
                                       request=request),
            'post': reverse(PostList.name,
                             request=request)
            })

