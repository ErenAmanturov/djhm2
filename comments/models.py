from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=False)
    stars = models.IntegerField()
    type = models.IntegerField(choices=(
        (1, 'Cars'),
        (2, 'Humans'),
        (3, 'Others')
    ), null=True)


class Comment(models.Model):
    author = models.CharField(max_length=15)
    commentary = models.TextField(max_length=35)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    rating = models.IntegerField(choices=(
        (1, 'Normal'),
        (2, 'Ok'),
        (3, 'bad'),
        (4, 'very bad')
    ), null=True)
