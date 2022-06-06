from rest_framework import filters
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from main_app.api.serializers.tags import TagSerializer
from taggit.models import Tag


class TagsView(GenericViewSet, ListModelMixin):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()