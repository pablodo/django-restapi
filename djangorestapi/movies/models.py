from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    aliases = models.CharField(max_length=200, blank=True, default="")  # JSON with list of aliases


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.PositiveSmallIntegerField()
    casting = models.ManyToManyField(Person, related_name='movies_acted')
    directors = models.ManyToManyField(Person, related_name='movies_directed')
    producers = models.ManyToManyField(Person, related_name='movies_produced')

