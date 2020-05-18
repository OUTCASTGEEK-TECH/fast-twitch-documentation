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
        only_fields = ['id', 'title', 'slug', 'date', 'intro', 'tags']

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
    article_by_slug = graphene.Field(ArticleNode, slug=graphene.String())
    articles_by_tag = graphene.List(ArticleNode, tag=graphene.String())

    @graphene.resolve_only_args
    def resolve_articles(self):
        articles = BlogPage.objects.live()
        return articles

    @graphene.resolve_only_args
    def resolve_article_by_slug(self, slug):
        article = BlogPage.objects.live().filter(slug=slug).first()
        return article

    @graphene.resolve_only_args
    def resolve_articles_by_tag(self, tag):
        articles = BlogPage.objects.live().filter(tags__name=tag)
        return articles

schema = graphene.Schema(query=Query)
