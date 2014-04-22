# coding: utf-8
from django.contrib import admin
from django import forms
from mikro_app.models import Tech_Info,Transport_Company,Orders,Static_Img,Contact,Static_Pages,Language 

label_transport_company=Tech_Info.objects.get(id=1).label_transport_company

def list_transport_company():
    list_name=list()    
    all_comp=Transport_Company.objects.count()
    if all_comp>0:
        for n in xrange(1,all_comp+1):
            comp_name=Transport_Company.objects.get(id=n).name
            list_name.append( (unicode(comp_name),unicode(comp_name)) )
        return list_name
    else:
        list_name.append( (u'свяжитесь с менеджером по поводу доставки',
                         u'свяжитесь с менеджером по поводу доставки') )
        return list_name



class Lang_Admin(admin.ModelAdmin):
    list_display=('lang_abbr','default')
    list_editable=('default',)


class Orders_Admin_Form(forms.ModelForm):
    transport_company=forms.ChoiceField(widget=forms.Select,#используем выпадающий список 
                                        choices=list_transport_company(), 
                                        label=label_transport_company 
                                        )                                                
    model=Orders

class Orders_Admin(admin.ModelAdmin):
    form=Orders_Admin_Form


admin.site.register(Tech_Info)
admin.site.register(Transport_Company)
admin.site.register(Orders,Orders_Admin)
admin.site.register(Static_Img)
admin.site.register(Contact)
admin.site.register(Static_Pages)
admin.site.register(Language,Lang_Admin)