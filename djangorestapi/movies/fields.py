from rest_framework import serializers

from . import models


class PersonField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return models.Person.objects.all()

    def to_representation(self, obj):
        return "{0} {1}".format(obj.first_name, obj.last_name)


