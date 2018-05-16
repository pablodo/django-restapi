from rest_framework import serializers
from drf_compound_fields import fields
import roman

from . import models


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    aliases =  fields.ListOrItemField(serializers.CharField())

    class Meta:
        model = models.Person
        fields = ('first_name', 'last_name', 'aliases')  # Manually sorted


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    release_year_roman = serializers.CharField()

    class Meta:
        model = models.Movie
        fields = (
            'title', 'release_year', 'release_year_roman', 'casting', 'directors', 'producers'
        )

    def validate(self, data):
        year = data['release_year']
        try:
            data['release_year_roman'] = roman.fromRoman(year)
        except roman.InvalidRomanNumeralError:
            raise serializers.ValidationError(
                "Invalid year {0}. Cannot convert to roman number".format(year)
            )
        return data
