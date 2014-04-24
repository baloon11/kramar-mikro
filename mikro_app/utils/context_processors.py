from django.conf import settings
from mikro_app.models import Tech_Info,Transport_Company,Static_Img,Static_Pages,Language
def my_vars(request):
    return {      
       # 'tech_info':Tech_Info.objects.get(id=1),
        'transport_company_context':Transport_Company.objects.all(),
        'static_img':Static_Img.objects.all(),
        'static_pages':Static_Pages.objects.all(),
        'all_languages':Language.objects.all(),
        'def_language':Language.objects.get(id=1).lang_abbr

           }
