# coding: utf-8
from django.contrib import admin
from django import forms
from mikro_app.models import (Tech_Info, Transport_Company, 
                              Orders, Static_Img, Contact,
                              Static_Pages, Language, Currency,
                              Country, PaymentMethod,Basic_Settings,
                              Social_Network,Static_Img_Text)

from django.core.exceptions import ObjectDoesNotExist

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



class Static_Img_Admin_Form(forms.ModelForm): 

    class Meta:
        model = Static_Img
        #fields = ['img', 'num','start']

    def __init__(self, *args, **kwargs):
        super(Static_Img_Admin_Form, self).__init__(*args, **kwargs)
        langs=Language.objects.all()     
        for lang in langs:
            if self.instance.pk is not None:
                static_image_text=Static_Img_Text.objects.filter(img=self.instance)
                text_instanse=static_image_text.get(lang=lang.lang_abbr)

                self.fields[lang.lang_abbr].initial=text_instanse.text

       # self.fields['num'].help_text=self.__dict__
       # self.fields['img'].help_text=Static_Img_Admin_Form.__dict__   


 #добавляем атрибуты непосредственно классу Static_Img_Admin_Form
langs=Language.objects.all().order_by('id')     
for lang in langs: # тут в цикле создаем поля к классу формы(не к экземпляру, а ко всему классу)
    lang_lang_abbr=lang.lang_abbr    
    Static_Img_Admin_Form.base_fields[lang_lang_abbr]=forms.CharField(label=lang_lang_abbr, max_length=400)
    Static_Img_Admin_Form.declared_fields[lang_lang_abbr]=forms.CharField(label=lang_lang_abbr, max_length=400) 

#-----------------------------
class Static_Img_Admin(admin.ModelAdmin):
    form = Static_Img_Admin_Form

    def save_model(self, request, obj, form, change):
        obj.save()
        langs=Language.objects.all().order_by('id')     
        for lang in langs:
            if change==False:#если  этот объект создается, а не изменяется, то создаем новую запись в Static_Img_Text
                Static_Img_Text.objects.create(text=form.cleaned_data[lang.lang_abbr],
                                               img=obj,
                                               lang=lang.lang_abbr)

            else: #если  этот объект изменяется, а не создается, то редактируем уже существующую запись в Static_Img_Text 
                static_image_text=Static_Img_Text.objects.filter(img=obj)# находим все экземпляры Static_Img_Text,  связанные с текущим экз модели obj
                text_instanse=static_image_text.get(lang=lang.lang_abbr)
                text_instanse.text=form.cleaned_data[lang.lang_abbr]
                text_instanse.save()



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

#================================
class Static_Pages_Form(forms.ModelForm):
    class Meta:
        model = Static_Pages

    def clean_num(self):
        try:
            Static_Pages.objects.get(lang=self.cleaned_data['lang'],num=self.cleaned_data['num'])
            raise forms.ValidationError(u'Для этого языка такой порядковый номер \
                                          стат. страницы уже существует ')
        except ObjectDoesNotExist:
            pass
    
        return self.cleaned_data['num']




#================================


class Static_Pages_Admin(admin.ModelAdmin):
    form = Static_Pages_Form
    list_filter = ('lang',)

admin.site.register(Tech_Info)
admin.site.register(Transport_Company)
admin.site.register(Orders, Orders_Admin)
admin.site.register(Static_Img,Static_Img_Admin)
admin.site.register(Contact, Contact_Admin)
admin.site.register(Static_Pages,Static_Pages_Admin)
admin.site.register(Language, Lang_Admin)
admin.site.register(Currency, Currency_Admin)
admin.site.register(Country, Country_Admin)
admin.site.register(PaymentMethod)
admin.site.register(Basic_Settings,Basic_Settings_Admin)
admin.site.register(Social_Network)
#admin.site.register(Static_Img_Text)

