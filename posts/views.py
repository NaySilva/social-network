from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
import json
from posts.models import Perfil, Post, Comment, Geo, Address
from posts.permissions import IsPostOrReadOnly, IsCommentOrReadOnly, IsPerfilOrReadOnly, IsUserOrReadOnly
from posts.serializers import PerfilSerializer, PostSerializer, CommentSerializer, PerfilDetailSerializer, \
    PostDetailSerializer, UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly,
    )


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly,
    )

class PerfilList(generics.ListCreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    name = 'perfil-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsPerfilOrReadOnly,
    )

class PerfilDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilDetailSerializer
    name = 'perfil-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsPerfilOrReadOnly,
    )

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsPostOrReadOnly,
    )

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    name = 'post-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsPostOrReadOnly,
    )

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'


    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsCommentOrReadOnly,
    )


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'


    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsCommentOrReadOnly,
    )


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request):
        return Response({
            'perfil': reverse(PerfilList.name,
                            request=request),
            'comment': reverse(CommentList.name,
                                       request=request),
            'post': reverse(PostList.name,
                             request=request),
            'user': reverse(UserList.name,
                             request=request)
            })
