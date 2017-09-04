import serializers as serializers
from django.contrib.auth.models import User
from rest_framework import serializers

from posts.models import Perfil, Post, Comment, Address, Geo


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email')


class GeoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Geo
        fields = ('id', 'lat', 'lng')


class AddressSerializer(serializers.ModelSerializer):

    geo = GeoSerializer()

    class Meta:
        model = Address
        fields = ('id', 'street', 'suite', 'city', 'zipcode', 'geo')


class PerfilSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(),
                                        slug_field="username")
    address = AddressSerializer()

    class Meta:
        model = Perfil
        fields = ('url', 'id', 'user', 'address')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    perfil = serializers.SlugRelatedField(queryset=Perfil.objects.all(),
                                          slug_field="username")

    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'body', 'perfil')


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    post = serializers.SlugRelatedField(queryset=Post.objects.all(),
                                        slug_field="title")

    class Meta:
        model = Comment
        fields = ('url', 'id', 'name', 'email', 'body', 'post')



class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    perfil = serializers.SlugRelatedField(queryset=Perfil.objects.all(),
                                          slug_field="username")

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'body', 'perfil', 'comments')



class PerfilDetailSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(),
                                        slug_field="username")

    posts = PostSerializer(many=True, read_only=True)
    address = AddressSerializer()

    class Meta:
        model = Perfil
        fields = ("url", "id", "user", "address", "posts")


