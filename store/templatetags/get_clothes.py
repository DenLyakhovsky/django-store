from django import template

from store.models import Category

register = template.Library()


@register.inclusion_tag('store/list_categories.html')
def get_clothes():
    categories_item = Category.objects.all()
    return {'categories_item': categories_item}
