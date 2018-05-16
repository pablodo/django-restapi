from rest_framework import serializers

from . import models


class PersonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Person
        fields = '__all__'


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Movie
        fields = '__all__'
