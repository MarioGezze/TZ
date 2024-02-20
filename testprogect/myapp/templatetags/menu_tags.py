from django import template
from ..models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent').select_related('parent__parent')

    def render_menu_item(item):
        is_active = item.url == request.path or (item.named_url and item.named_url == request.resolver_match.url_name)
        children = item.children.all()

        return {
            'item': item,
            'is_active': is_active,
            'children': [render_menu_item(child) for child in children],
        }

    menu_data = [render_menu_item(item) for item in menu_items.filter(parent=None)]

    return {
        'menu_data': menu_data,
    }
