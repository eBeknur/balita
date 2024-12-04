from balitassap.models import Category, Tags
from django import template


register = template.Library()

@register.simple_tag()
def categories():
    return Category.objects.all()

@register.simple_tag()
def tags():
    return Tags.objects.all()
