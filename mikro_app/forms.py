# -*- coding: utf-8 -*-
from django import forms
from mikro_app.models import Tech_Info, Transport_Company, Country, PaymentMethod, Orders
#from django.contrib.auth.models import User
from django.forms.widgets import Input


def list_transport_company():
    list_name = list()
    all_comp = Transport_Company.objects.count()
    for n in xrange(1, all_comp + 1):
        comp_name = Transport_Company.objects.get(id=n).name
        # unicode(comp_name)
        list_name.append((unicode(comp_name), unicode(comp_name)))
    return list_name


def list_num():
    num = list()
    for n in xrange(1, 11):
        n = unicode(n)
        num.append((n, n))
    return num


def all_countries():
    all_countries = list()
    for country_ins in Country.objects.all():
        all_countries.append(
            (unicode(country_ins.country), unicode(country_ins.country)))
    return all_countries

def list_payment_method(): 
    all_payment_methods = list()
    for payment_method_ins in PaymentMethod.objects.all():
        all_payment_methods.append((unicode(payment_method_ins.payment_method),
                                    unicode(payment_method_ins.payment_method))
                                   )
    return all_payment_methods



def list_payment_method_my_country(lang):
    text = Tech_Info.objects.get(lang__lang_abbr=lang)
    all_payment_methods = list()
    all_payment_methods.append((text.cod_text, text.cod_text))
    for payment_method_ins in PaymentMethod.objects.all():
        all_payment_methods.append((unicode(payment_method_ins.payment_method),
                                    unicode(payment_method_ins.payment_method))
                                   )
    return all_payment_methods


class Homepage_Form(forms.Form):
    num = forms.ChoiceField(widget=forms.Select, choices=list_num())
    country = forms.ChoiceField(widget=forms.Select, choices=all_countries())


class Homepage_Form_Unique(forms.Form):
    country = forms.ChoiceField(widget=forms.Select, choices=all_countries())


class Orders_Form(forms.ModelForm):

    additional_information = forms.CharField(max_length=10000,
                                             widget=forms.Textarea(
                                                 attrs={'cols': 60, 'rows': 8})
                                             )
    payment_method = forms.ChoiceField(widget=forms.Select)                                        

    class Meta:
        model = Orders
        fields = ('fio', 'tel', 'city', 'transport_company',
                  'payment_method', 'additional_information')

    def __init__(self, *args, **kwargs):
        country_ins = kwargs.pop('country', None)
        super(Orders_Form, self).__init__(*args, **kwargs)
        self.fields['transport_company'].queryset = Transport_Company.objects.filter(country__country=country_ins)
        self.fields['payment_method'].choices = list_payment_method()

class Orders_Form_My_Country(forms.ModelForm):

    additional_information = forms.CharField(max_length=10000,
                                             widget=forms.Textarea(
                                                 attrs={'cols': 60, 'rows': 8})
                                             )

    payment_method = forms.ChoiceField(widget=forms.Select)

    class Meta:
        model = Orders
        fields = ('fio', 'tel', 'city', 'transport_company',
                  'payment_method', 'additional_information')

    def __init__(self, *args, **kwargs):
        country = kwargs.pop('country', None)
        lang = kwargs.pop('lang', None)
        super(Orders_Form_My_Country, self).__init__(*args, **kwargs)
        self.fields['transport_company'].queryset = Transport_Company.objects.filter(country__country=country)
        self.fields['payment_method'].choices = list_payment_method_my_country(lang)


class Contacts (forms.Form):
    contact_subject = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    text = forms.CharField(max_length=10000,
                           widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
