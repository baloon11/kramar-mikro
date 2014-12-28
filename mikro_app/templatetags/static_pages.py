from django import template
from mikro_app.models import Static_Pages, Language
register = template.Library()

@register.inclusion_tag('show_static_pages.html')
def static_pages(lang='',curr=''):
    return {'static_pages' :Static_Pages.objects.filter(lang=Language.objects.get(lang_abbr=lang)),
            'curr':curr
            }
   