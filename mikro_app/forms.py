# -*- coding: utf-8 -*-
from django import forms
from mikro_app.models import Tech_Info,Transport_Company
#from django.contrib.auth.models import User
from django.forms.widgets import Input
 
class NumberInput(Input):
#HTML5 Number Input."""
    input_type = 'number'


def list_transport_company():
    list_name=list()
    all_comp=Transport_Company.objects.count()
    for n in xrange(1,all_comp+1):
        comp_name=Transport_Company.objects.get(id=n).name
        list_name.append( (unicode(comp_name),unicode(comp_name)) ) #unicode(comp_name)
    return list_name

def list_num():
    num=list()
    for n in xrange(1,11):
        n=unicode(n)
        num.append((n,n))
    return num     
   


def list_cod_or_bankcard():
    return [(u'наложенный платеж',u'наложенный платеж'),(u'банковская карта',u'банковская карта')]

label_buy_num=Tech_Info.objects.get(id=1).label_buy_num
label_fio=Tech_Info.objects.get(id=1).label_fio
label_tel=Tech_Info.objects.get(id=1).label_tel
label_city=Tech_Info.objects.get(id=1).label_city
label_transport_company=Tech_Info.objects.get(id=1).label_transport_company

label_cod_or_bankcard=Tech_Info.objects.get(id=1).label_cod_or_bankcard
info_cod_or_bankcard=Tech_Info.objects.get(id=1).info_cod_or_bankcard

label_additional_information=Tech_Info.objects.get(id=1).label_additional_information
info_additional_information=Tech_Info.objects.get(id=1).info_additional_information

label_contacts_subject=Tech_Info.objects.get(id=1).label_contacts_subject
label_contacts_name=Tech_Info.objects.get(id=1).label_contacts_name
label_contacts_email=Tech_Info.objects.get(id=1).label_contacts_email
label_contacts_text=Tech_Info.objects.get(id=1).label_contacts_text


class Homepage_Form(forms.Form):
    num=forms.ChoiceField(label=label_buy_num,widget=forms.Select, choices=list_num()) 

#class Homepage_Form_Unique(forms.Form):
#    pass


class Orders_Form(forms.Form):
    fio=forms.CharField(label=label_fio,max_length=100)
    tel=forms.CharField(label=label_tel,max_length=20)
    city=forms.CharField(label=label_city,max_length=100)
    transport_company = forms.ChoiceField(widget=forms.Select,#используем выпадающий список 
                                                 choices=list_transport_company(),
                                                 label=label_transport_company,
                                                 ) 

    cod_or_bankcard=forms.ChoiceField(widget=forms.Select,#используем выпадающий список 
                                                 choices=list_cod_or_bankcard(),
                                                 label=label_cod_or_bankcard,
                                                 help_text=info_cod_or_bankcard) 
    
    additional_information=forms.CharField(label=label_additional_information,
                                           max_length=10000,
                                           help_text=info_additional_information,
                                           widget=forms.Textarea(attrs={'cols': 60, 'rows':8}) )
    def clean_cod_or_bankcard(self):
        cod_or_bankcard_in_form=self.cleaned_data['cod_or_bankcard']
        transport_company_in_form=self.cleaned_data['transport_company']
        transport_company_in_model=Transport_Company.objects.get(name=transport_company_in_form)

        if (cod_or_bankcard_in_form==u'наложенный платеж') and (transport_company_in_model.cod==False):
            raise forms.ValidationError(u"Доставка наложенным платежем с этой транспортной компанией невозможна.")
        return cod_or_bankcard_in_form    





#class Confirmation(forms.Form):
#   pass

class Contacts (forms.Form):
    contact_subject=forms.CharField(label=label_contacts_subject,max_length=100)
    name=forms.CharField(label=label_contacts_name,max_length=100)
    email=forms.EmailField(label=label_contacts_email)
    text=forms.CharField(label=label_contacts_text,max_length=10000,
                         widget=forms.Textarea(attrs={'cols': 60, 'rows':10}) )


     
                                           
                                          
