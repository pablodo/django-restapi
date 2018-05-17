import json
import functools

from django.core.serializers import serialize
from rest_framework import serializers

from . import models

json_serializer = functools.partial(serialize, 'json')


class BaseField(serializers.PrimaryKeyRelatedField):

    def to_representation(self, obj):
        # Ugly workaround to make it work with both HTML version
        # this should only perform a `return str(obj)` but then
        # it cannot be interpreted by `to_internal_value` because
        # it receives a string instead of the full object
        data = json_serializer([obj])
        struct = json.loads(data)[0]
        return json.dumps(struct)

    def to_internal_value(self, data):
        if isinstance(data, int):
            return data
        else:
            obj = json.loads(data)
            return obj['pk']


class PersonField(BaseField):
    def get_queryset(self):
        return models.Person.objects.all()


class MovieField(BaseField):
    def get_queryset(self):
        return models.Movie.objects.all()

