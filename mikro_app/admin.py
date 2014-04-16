# coding: utf-8
from django.contrib import admin
from django import forms
from mikro_app.models import Tech_Info,Transport_Company,Orders,Static_Img,Contact,Static_Pages,Language 

def list_lang():
    list_name=list()
    all_lang=Language.objects.count()
    if all_lang>0:
        for l in xrange(1,all_lang+1):
            lang_abbr=Language.objects.get(id=l).lang_abbr
            list_name.append( (unicode(lang_abbr),unicode(lang_abbr)) ) 
        return list_name
    else:
        list_name.append( (u'этот язык будет использован по умолчанию',
                           u'этот язык будет использован по умолчанию') )
        return list_name 

class Tech_Info_Form_Choice(forms.ModelForm):	
    lang=forms.ChoiceField(widget=forms.Select,choices=list_lang()) 
    class Meta:
        model = Tech_Info
    
class Tech_Info_Form_Char_Default(forms.ModelForm):
    lang=forms.CharField(label=u'язык,установленный в системе по умолчанию')
    class Meta:
        model = Tech_Info
    
class Tech_Info_Form_Char(forms.ModelForm):
    lang=forms.CharField(label=u'Language')
    class Meta:
        model = Tech_Info

def one_or_more_languages():
    if Tech_Info.objects.count()>1:
    	for all_tech_info in Tech_Info.objects.all():
    		if all_tech_info.id>1:
    			return Tech_Info_Form_Choice
    		elif all_tech_info.id==1:
    			return Tech_Info_Form_Char
    else:
    	return Tech_Info_Form_Char_Default


class Tech_Info_Admin(admin.ModelAdmin):
    form =one_or_more_languages()

admin.site.register(Tech_Info,Tech_Info_Admin)
admin.site.register(Transport_Company)
admin.site.register(Orders)
admin.site.register(Static_Img)
admin.site.register(Contact)
admin.site.register(Static_Pages)
admin.site.register(Language)