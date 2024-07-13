from django import template

register = template.Library()


@register.filter
def media_path(data):
    if data:
        return f"/media/{data}"
    return "#"
