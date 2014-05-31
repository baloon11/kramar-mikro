from django.conf import settings
from mikro_app.models import Tech_Info,Static_Img,Static_Pages,Language,Currency,Basic_Settings
def all_languages():
	all_languages=list()
	for tech_info in Tech_Info.objects.all():
		all_languages.append(tech_info.lang)
	return all_languages

def all_currencies():
	all_currencies=list()
	for currency in Currency.objects.all():
		all_currencies.append(currency.curr_abbr)
	return all_currencies



def my_vars(request):
    return {      
        'static_img':Static_Img.objects.all(),
        'static_pages':Static_Pages.objects.all(),
        'all_languages':all_languages(),
        'all_currencies':all_currencies(),
        'basic_settings':Basic_Settings.objects.get(id=1)
           }
