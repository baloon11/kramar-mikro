from django import template
from mikro_app.models import Transport_Company

register = template.Library()
@register.inclusion_tag("transport_company_list.html")
def all_transport_companies_tag():
    transport_company=Transport_Company.objects.all()
    return {'all_transport_companies': transport_company}



