# coding: utf-8
from django.contrib import admin
from django import forms
from mikro_app.models import Tech_Info,Transport_Company,Orders,Static_Img,Contact,Static_Pages,Language 

def list_lang():
    list_name=list()
    all_lang=Language.objects.count()
    
    for l in xrange(1,all_lang+1):
        lang_abbr=Language.objects.get(id=l).lang_abbr
        list_name.append((u'rus',u'rus'))
        list_name.append((unicode(lang_abbr),unicode(lang_abbr)) ) 
    return list_name
    
class Tech_Info_Form_Choice(forms.ModelForm):   
    lang=forms.ChoiceField(label=u'Language',widget=forms.Select,choices=list_lang()) 
    class Meta:
        model = Tech_Info
'''  
class Tech_Info_Form_Char_Default(forms.ModelForm):
    lang=forms.CharField(label=u'язык,установленный в системе по умолчанию')
    class Meta:
        model = Tech_Info'''
    
class Tech_Info_Form_Char(forms.ModelForm):
    lang=forms.CharField(label=u'Language')
    class Meta:
        model = Tech_Info
'''
def one_or_more_languages():
    if Tech_Info.objects.count()>1:
        for all_tech_info in Tech_Info.objects.all():
            if all_tech_info.id>1:
                return Tech_Info_Form_Choice
            elif all_tech_info.id==1:
                return Tech_Info_Form_Char
    else:
        return Tech_Info_Form_Char_Default

def readonly():
    if one_or_more_languages()==Tech_Info_Form_Char_Default:
        readonly_fields_list = ('lang',)
    else:
        readonly_fields_list = tuple()

    return readonly_fields_list'''



def one_or_more_languages():
    #if Tech_Info.objects.count()==1:
      #  return [Tech_Info_Form_Char_Default,('lang',)]

    if Language.objects.count()>0:
        return [Tech_Info_Form_Choice,list()]
    else:
        return [Tech_Info_Form_Char,list()]
            

class Tech_Info_Admin(admin.ModelAdmin):
    form =one_or_more_languages()[0]
   # readonly_fields=one_or_more_languages()[1]

admin.site.register(Tech_Info,Tech_Info_Admin)
admin.site.register(Transport_Company)
admin.site.register(Orders)
admin.site.register(Static_Img)
admin.site.register(Contact)
admin.site.register(Static_Pages)
admin.site.register(Language)