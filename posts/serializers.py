import serializers as serializers
from rest_framework import serializers

from posts.models import User, Post, Comment, Address, Geo


class GeoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Geo
        fields = ('url', 'id', 'lat', 'lng')


class AddressSerializer(serializers.ModelSerializer):

    geo = GeoSerializer()

    class Meta:
        model = Address
        fields = ('url', 'id', 'street', 'suite', 'city', 'zipcode', 'geo')


class UserSerializer(serializers.ModelSerializer):

    address = AddressSerializer()

    class Meta:
        model = User
        fields = ('url', 'id', 'name', 'email', 'address')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(),
                                        slug_field="name")

    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'body', 'user')



class CommentSerializer(serializers.HyperlinkedModelSerializer):

    post = serializers.SlugRelatedField(queryset=Post.objects.all(),
                                        slug_field="title")

    class Meta:
        model = Comment
        fields = ('url', 'id', 'name', 'email', 'body', 'post')



class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(),
                                        slug_field="name")

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'body', 'user', 'comments')



class UserDetailSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True, read_only=True)
    address = AddressSerializer()

    class Meta:
        model = User
        fields = ("url", "id", "username", "email", "name", "address", "posts")


