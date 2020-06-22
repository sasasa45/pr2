from django import template
from item.models import Items
register=template.Library()

@register.filter(name='quantity')
def quantity(value, session):
    return session[str(value)]
@register.filter(name='subtotal')
def subtotal (value,session):
    return Items.objects.get(pk=value).price*session[str(value)]
@register.filter(name='total')
def total (value,session):
    suma=0
    for i in value:
        suma+=i.price*session[str(i.pk)]
    return suma
