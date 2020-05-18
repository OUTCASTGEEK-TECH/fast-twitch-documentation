import graphene
from graphene_django import DjangoObjectType
from blog.models import BlogPage
from graphene.types.generic import GenericScalar

from django.db import models
from api import graphene_wagtail

class ParagraphBlock(graphene.ObjectType):
    value = GenericScalar()

class HeadingBlock(graphene.ObjectType):
    value = GenericScalar()

class CodeBlock(graphene.ObjectType):
    value = GenericScalar()

class BlogPageBody(graphene.Union):
    class Meta:
        types = (ParagraphBlock, HeadingBlock, CodeBlock)

class ArticleNode(DjangoObjectType):
    body = graphene.List(BlogPageBody)

    class Meta:
        model = BlogPage
        only_fields = ['id', 'title', 'date', 'intro', 'tags']

    def resolve_body(self, info):
        repr_body = []
        for block in self.body.stream_data:
            block_type = block.get('type')
            value = block.get('value')
            if block_type == 'paragraph':
                repr_body.append(ParagraphBlock(value=value))
            elif block_type == 'heading':
                repr_body.append(HeadingBlock(value=value))
            elif block_type == 'code':
                repr_body.append(CodeBlock(value=value))
        return repr_body

class Query(graphene.ObjectType):
    articles = graphene.List(ArticleNode)
    articles_by_tag = graphene.List(ArticleNode, tag=graphene.String())

    @graphene.resolve_only_args
    def resolve_articles(self):
        return BlogPage.objects.live()

    @graphene.resolve_only_args
    def resolve_articles_by_tag(self, tag):
        return BlogPage.objects.live().filter(tags__name=tag)

schema = graphene.Schema(query=Query)
