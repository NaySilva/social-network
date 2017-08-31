from django.db import models

# Create your models here.

class Geo(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return ('%f - %f' % (self.lat, self.lng))


class Address(models.Model):
    street = models.CharField(max_length=120)
    suite = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=120)
    geo = models.ForeignKey(Geo)

    def __str__(self):
        return self.street



class User(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.ForeignKey(Address)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    user = models.ForeignKey(User, related_name='posts')

    def __str__(self):
        return self.title



class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, related_name='comments')

    def __str__(self):
        return self.name


