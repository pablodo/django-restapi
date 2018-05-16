from rest_framework import viewsets
from rest_framework import authentication, permissions

from . import serializers, models


class AuthMixin(object):

    UNSAFE_ACTIONS = ('destroy', 'create', 'update', 'partial_update')

    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.BasicAuthentication,
    )

    def get_permissions(self):
        permissions_classes = []
        if self.action in self.UNSAFE_ACTIONS:
            permissions_classes.append(permissions.IsAuthenticated)
        return [p() for p in permissions_classes]


class MovieViewSet(AuthMixin, viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class PersonViewSet(AuthMixin, viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


