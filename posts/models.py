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



class Perfil(models.Model):
    user = models.ForeignKey('auth.User',default='1')
    address = models.ForeignKey(Address)

    @property
    def username(self):
        return self.user.username

    @property
    def email(self):
        return self.user.email

    def __str__(self):
        return self.user.username



class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    perfil = models.ForeignKey(Perfil, related_name='posts')

    def __str__(self):
        return self.title



class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


