from django.db import models

# Create your models here.

from wagtail.core import blocks
from wagtail.snippets.models import register_snippet
from wagtailmarkdown.blocks import MarkdownBlock
from wagtail.core.models import Page
from wagtail.core.fields import (
    RichTextField,
    StreamField
)
from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel
)

from modelcluster.fields import (
    ParentalKey,
    ParentalManyToManyField
)
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import (
    TaggedItemBase,
    Tag as TaggitTag
)

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='page_tags',
    )

@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True

class BlogPage(Page):
    date = models.DateField("Post Date")
    intro = models.CharField(max_length=250)
    tags = ClusterTaggableManager(through='blog.BlogPageTag', blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('code', MarkdownBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('tags'),
        FieldPanel('date'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]
