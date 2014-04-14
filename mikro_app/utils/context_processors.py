from django.conf import settings
from mikro_app.models import Tech_Info,Transport_Company,Static_Img
def my_vars(request):
    return {      
        'tech_info':Tech_Info.objects.get(id=1),
        'transport_company_context':Transport_Company.objects.all(),
        'static_img':Static_Img.objects.all()
           }