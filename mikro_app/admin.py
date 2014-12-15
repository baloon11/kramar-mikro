# coding: utf-8
from django.contrib import admin
from django import forms
from mikro_app.models import Tech_Info, Transport_Company, Orders, Static_Img, Contact, Static_Pages, Language, Currency, Country, PaymentMethod,Basic_Settings,Social_Network

label_transport_company = Tech_Info.objects.get(id=1).label_transport_company


def list_transport_company():
    list_name = list()
    all_comp = Transport_Company.objects.count()
    if all_comp > 0:
        for n in xrange(1, all_comp + 1):
            comp_name = Transport_Company.objects.get(id=n).name
            list_name.append((unicode(comp_name), unicode(comp_name)))
        return list_name
    else:
        list_name.append((u'свяжитесь с менеджером по поводу доставки',
                          u'свяжитесь с менеджером по поводу доставки'))
        return list_name
"""
def list_payment_method():
    payment_method_list=[(u'банковская карта',u'банковская карта'),
                        (u'наложенный платеж',u'наложенный платеж') ]
    return payment_method_list"""


def list_is_it_close():
    is_it_close_list = [(u'новый заказ', u'новый заказ'),
                        (u'в обработке', u'в обработке'),
                        (u'обработанный', u'обработанный')]
    return is_it_close_list


def contact_is_it_close():
    is_it_close_list = [(u'не прочитано', u'не прочитано'),
                        (u'прочитано', u'прочитано')]
    return is_it_close_list


class LangAdminForm(forms.ModelForm):
    model = Language

    def clean_default(self):

        if self.cleaned_data['default'] == True and Language.objects.filter(default=self.cleaned_data['default']).count() == 1:
            raise forms.ValidationError(u'Язык по умолчанию уже выставлен')
        return self.cleaned_data['default']


class Lang_Admin(admin.ModelAdmin):
    list_display = ('lang_abbr', 'default')
    form = LangAdminForm


class CurrencyAdminForm(forms.ModelForm):
    model = Currency

    def clean_default(self):

        if self.cleaned_data['default'] == True and Currency.objects.filter(default=self.cleaned_data['default']).count() == 1:
            raise forms.ValidationError(u'Валюта по умолчанию уже выставлена')
        return self.cleaned_data['default']


class Currency_Admin(admin.ModelAdmin):
    list_display = ('curr_abbr', 'curr_price', 'default')
    list_editable = ('curr_price',)
    form = CurrencyAdminForm


class Currency_for_Transport_Company_Admin(admin.ModelAdmin):
    list_display = ('curr_abbr',)
   # list_editable=('default','curr_price')


class Country_Admin(admin.ModelAdmin):
    list_display = ('country', 'is_it_your_country',)
    list_editable = ('is_it_your_country',)


class Orders_Admin_Form(forms.ModelForm):
    transport_company = forms.ChoiceField(widget=forms.Select,  # используем выпадающий список
                                          choices=list_transport_company(),
                                          label=label_transport_company
                                          )
# payment_method=forms.ChoiceField(widget=forms.Select,#используем выпадающий список
#                                        choices=list_payment_method(),
#                                        label=label_cod_or_bankcard
#                                        )
    is_it_close = forms.ChoiceField(widget=forms.Select,  # используем выпадающий список
                                    choices=list_is_it_close(),
                                    label=u"Cтатус заказа"
                                    )
    model = Orders


class Contact_Admin_Form(forms.ModelForm):
    is_it_close = forms.ChoiceField(widget=forms.Select,  # используем выпадающий список
                                    choices=contact_is_it_close(),
                                    label=u"Прочитано ли письмо"
                                    )
    model = Contact

#------------------------------

#class Static_Img_Admin_Form_Parent(forms.ModelForm):
#    pass

#langs=Language.objects.all()     
#for lang in langs: # тут в цикле создаем поля  к  классу формы( не к экземпляру, а ко всему классу)
#    lang_lang_abbr=lang.lang_abbr    
#    Static_Img_Admin_Form_Parent.lang_lang_abbr=forms.CharField(label=lang_lang_abbr, max_length=400)

# затем  передадим Static_Img_Admin_Form_Parent как родительский 
# в Static_Img_Admin_Form -и в нем у нас будут уже доп поля   -не Static_Img_Admin_Form видит род атрибуты в админке
#  по идее правильно-- в таком варианте нет нужды обращаться к атрибутам родительского класса
#lang_abbr_list=[]

#langs=Language.objects.all()     
#for lang in langs:
#    lang_abbr_list.append(lang.lang_abbr)



class Static_Img_Admin_Form(forms.ModelForm): 

#    for lang in xrange(1,11):
#        lang=str(lang)
#        obj.lang=forms.CharField(max_length=400)
    
#    lang=forms.CharField(max_length=400)

    class Meta:
        model = Static_Img
        #fields = ['img', 'num','start']

    def __init__(self, *args, **kwargs):
        super(Static_Img_Admin_Form, self).__init__(*args, **kwargs)
        langs=Language.objects.all()     
        for lang in langs: # тут в цикле создаем доп поля в форме 
            self.fields[lang.lang_abbr]=forms.CharField(label=lang.lang_abbr, max_length=400)
#            self.Meta.fields.append(lang.lang_abbr)
        self.fields['num'].help_text=self.__dict__
        self.fields['img'].help_text=Static_Img_Admin_Form.__dict__   


#    def __init__(self, *args, **kwargs):
#        super(Static_Img_Admin_Form, self).__init__(*args, **kwargs)
#        self.fields['num'].help_text=self.__dict__#.update( super(Static_Img_Admin_Form, self).__dict__ ) 
#        self.fields['img'].help_text=Static_Img_Admin_Form.__dict__   


 #попробуем додавить  атрибуты непосредственно классу Static_Img_Admin_Form
langs=Language.objects.all()     
for lang in langs: # тут в цикле создаем поля к классу формы( не к экземпляру, а ко всему классу)
    lang_lang_abbr=lang.lang_abbr    
    Static_Img_Admin_Form.base_fields[lang_lang_abbr]=forms.CharField(label=lang_lang_abbr, max_length=400)
    Static_Img_Admin_Form.declared_fields[lang_lang_abbr]=forms.CharField(label=lang_lang_abbr, max_length=400) 

#-----------------------------
class Static_Img_Admin(admin.ModelAdmin):
    form = Static_Img_Admin_Form


#    def get_fieldsets(self, request, obj=None):
#        fieldsets = super(Static_Img_Admin, self).get_fieldsets(request, obj)

#        langs=Language.objects.all()
#        for lang in langs:
#            fieldsets[0][1]['fields'] +=(lang.lang_abbr,) # тут используем такой же цикл как выше 
                                                          # (плучаем такие же значения) и добавляем в админку.
#        return fieldsets


 #   def get_form(self, request, obj=None, **kwargs):
 #       langs=Language.objects.all()     
 #       self.fields=[]
 #       for lang in langs: # тут в цикле добавляем  доп поля в форме в админке    
 #           self.fields.append(lang.lang_abbr)

  #      return super(Static_Img_Admin, self).get_form(request, obj, **kwargs)
#-----------------------------

class Orders_Admin(admin.ModelAdmin):
    form = Orders_Admin_Form



class Contact_Admin(admin.ModelAdmin):
    form = Contact_Admin_Form
    list_display = ('date_time', 'contact_subject', 'is_it_close')
    list_display_links = ('date_time', 'contact_subject', 'is_it_close')


class Basic_Settings_Admin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super(Basic_Settings_Admin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )

    list_display = ('title','unique','email') 
    list_editable = ('unique','email')    
    model = Basic_Settings



admin.site.register(Tech_Info)
admin.site.register(Transport_Company)
admin.site.register(Orders, Orders_Admin)
admin.site.register(Static_Img,Static_Img_Admin)
admin.site.register(Contact, Contact_Admin)
admin.site.register(Static_Pages)
admin.site.register(Language, Lang_Admin)
admin.site.register(Currency, Currency_Admin)
admin.site.register(Country, Country_Admin)
admin.site.register(PaymentMethod)
admin.site.register(Basic_Settings,Basic_Settings_Admin)
admin.site.register(Social_Network)
