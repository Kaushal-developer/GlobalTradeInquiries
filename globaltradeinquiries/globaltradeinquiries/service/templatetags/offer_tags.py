# myapp/templatetags/offer_tags.py
from django import template
from service.models import Offer

register = template.Library()

@register.simple_tag
def get_active_offers():
    print(Offer.objects.filter(is_active=True).order_by('start_time'))
    return Offer.objects.filter(is_active=True).order_by('start_time')
