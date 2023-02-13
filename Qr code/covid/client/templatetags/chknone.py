from django import template
from client.models import *

register = template.Library()
@register.filter(name='nonechk')
def nonechk(chk):
    if chk==None:
        return "Not selected"
    else:
        return chk