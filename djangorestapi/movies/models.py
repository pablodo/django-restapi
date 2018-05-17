from django.db import models
import roman


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    aliases = models.CharField(max_length=200, blank=True, default="")  # JSON with list of aliases

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.PositiveSmallIntegerField()
    casting = models.ManyToManyField(Person, related_name='movies_acted')
    directors = models.ManyToManyField(Person, related_name='movies_directed')
    producers = models.ManyToManyField(Person, related_name='movies_produced')

    def __str__(self):
        return "{0} {1}".format(self.title, self.release_year)

    def release_year_roman(self):
        return roman.toRoman(self.release_year)


