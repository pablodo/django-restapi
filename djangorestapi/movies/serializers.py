from rest_framework import serializers
from drf_compound_fields import fields as drf_fields
import roman

from . import models
from . import fields


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    aliases = drf_fields.ListOrItemField(serializers.CharField(), required=False)

    class Meta:
        model = models.Person
        fields = ('id', 'first_name', 'last_name', 'aliases')  # Manually sorted


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    release_year_roman = serializers.CharField(required=False)
    casting = fields.PersonField(many=True)
    directors = fields.PersonField(many=True)
    producers = fields.PersonField(many=True)

    class Meta:
        model = models.Movie
        fields = (
            'id', 'title', 'release_year', 'release_year_roman',
            'casting', 'directors', 'producers'
        )

    def validate(self, data):
        year = data['release_year']
        try:
            roman.toRoman(year)
        except roman.InvalidRomanNumeralError:
            raise serializers.ValidationError(
                "Invalid year {0}. Cannot convert to roman number".format(year)
            )
        return data

