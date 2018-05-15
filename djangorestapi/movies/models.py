from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    last_name = models.CharField()
    first_name = models.CharField()
    aliases = models.CharField()  # JSON with list of aliases


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField()
    release_year = models.PositiveSmallIntegerField()
    casting = models.ManytoManyField(Person)
    directors = models.ManytoManyField(Person)
    producers = models.ManytoManyField(Person)
