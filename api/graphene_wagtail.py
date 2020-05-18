from wagtail.core.fields import StreamField
import graphene
from graphene.types import (
    Scalar,
    String
)

from graphene_django.converter import convert_django_field

from modelcluster.contrib.taggit import ClusterTaggableManager

class GenericStreamFieldType(Scalar):
    @staticmethod
    def serialize(stream_value):
        return stream_value.stream_data

@convert_django_field.register(StreamField)
def convert_stream_field(field, registry=None):
    return GenericStreamFieldType(
        description=field.help_text, required=not field.null
    )


class FlatTags(String):

    @classmethod
    def serialize(cls, value):
        tagsList = []
        for tag in value.all():
            tagsList.append(tag.name)
        return tagsList


@convert_django_field.register(ClusterTaggableManager)
def convert_tag_field_to_string(field, registry=None):
    return graphene.Field(FlatTags,
                          description=field.help_text,
                          required=not field.null)
