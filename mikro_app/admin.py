# coding: utf-8
from django.contrib import admin
from django import forms
from mikro_app.models import Tech_Info,Transport_Company,Orders,Static_Img,Contact,Static_Pages,Language,Currency,Country 

label_transport_company=Tech_Info.objects.get(id=1).label_transport_company
label_cod_or_bankcard=Tech_Info.objects.get(id=1).label_cod_or_bankcard

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

def list_payment_method():
    payment_method_list=[(u'банковская карта',u'банковская карта'),
                        (u'наложенный платеж',u'наложенный платеж') ]
    return payment_method_list

def list_is_it_close():
    is_it_close_list=[(u'новый заказ',u'новый заказ'),
                      (u'в обработке',u'в обработке'),
                     (u'обработанный',u'обработанный') ]
    return is_it_close_list

def contact_is_it_close():
    is_it_close_list=[(u'не прочитано',u'не прочитано'),
                      (u'прочитано',u'прочитано') ]
    return is_it_close_list 


class Lang_Admin(admin.ModelAdmin):
    list_display=('lang_abbr','default')
    list_editable=('default',)

class Currency_Admin(admin.ModelAdmin):
    list_display=('curr_abbr','default','curr_price')
    list_editable=('default','curr_price')

class Currency_for_Transport_Company_Admin(admin.ModelAdmin):
    list_display=('curr_abbr',)
   # list_editable=('default','curr_price')




class Orders_Admin_Form(forms.ModelForm):
    transport_company=forms.ChoiceField(widget=forms.Select,#используем выпадающий список 
                                        choices=list_transport_company(), 
                                        label=label_transport_company 
                                        )  
    payment_method=forms.ChoiceField(widget=forms.Select,#используем выпадающий список 
                                        choices=list_payment_method(), 
                                        label=label_cod_or_bankcard 
                                        ) 
    is_it_close=forms.ChoiceField(widget=forms.Select,#используем выпадающий список 
                                        choices=list_is_it_close(), 
                                        label=u"Cтатус заказа" 
                                        )   
    model=Orders


class Contact_Admin_Form(forms.ModelForm):
    is_it_close=forms.ChoiceField(widget=forms.Select,#используем выпадающий список 
                                        choices=contact_is_it_close(), 
                                        label=u"Прочитано ли письмо" 
                                        )
    model=Contact

class Orders_Admin(admin.ModelAdmin):
    form=Orders_Admin_Form

class Contact_Admin(admin.ModelAdmin):
    form=Contact_Admin_Form


admin.site.register(Tech_Info)
admin.site.register(Transport_Company)
admin.site.register(Orders,Orders_Admin)
admin.site.register(Static_Img)
admin.site.register(Contact,Contact_Admin)
admin.site.register(Static_Pages)
admin.site.register(Language,Lang_Admin)
admin.site.register(Currency,Currency_Admin)
admin.site.register(Country)
