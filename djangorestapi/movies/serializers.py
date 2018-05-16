from rest_framework import serializers
from drf_compound_fields import fields

from . import models


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    aliases =  fields.ListOrItemField(serializers.CharField())

    class Meta:
        model = models.Person
        fields = ('first_name', 'last_name', 'aliases')  # Manually sorted


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Movie
        fields = '__all__'
