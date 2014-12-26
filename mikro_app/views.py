# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from mikro_app.models import (Tech_Info, Transport_Company,
                              Orders, Contact, 
                              Static_Pages,Static_Img,Static_Img_Text,
                              Language, Currency, Country,
                              PaymentMethod,Basic_Settings)


from mikro_app.forms import (Homepage_Form, Homepage_Form_Unique,
                             Orders_Form, Orders_Form_My_Country, Contacts)

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def lang_id(lang):
    def_lang = Language.objects.filter(default=True)
    if def_lang.count() == 1:

        if lang == '':  # для першої сторінки
            one_lang_abbr = Language.objects.get(default=True).lang_abbr
            tech_info = Tech_Info.objects.get(lang__lang_abbr=one_lang_abbr)
        else:
            # для всіх інших
            tech_info = Tech_Info.objects.get(lang__lang_abbr=lang)

    if def_lang.count() == 0:  # якщо мова за замовчуванням не задана
        tech_info = Tech_Info.objects.get(id=1)

    return tech_info


def lang_def(lang):
    if lang == '':
        lang_abbr = Language.objects.get(default=True).lang_abbr
    else:
        lang_abbr = lang
    return lang_abbr


def start(request, lang='', curr=''):
    tech_info = lang_id(lang)
    lang = lang_def(lang)

    static_img_list=[]
    static_img=Static_Img.objects.all()
    for st_img in static_img:
      img_text_instance=Static_Img_Text.objects.get(lang=lang,img=st_img)
      static_img_list.append([st_img,img_text_instance.text]) 


    if Basic_Settings.objects.get(id=1).unique == True:
        if request.method == 'POST':
            form = Homepage_Form_Unique(request.POST)
            if form.is_valid():
                fcd = form.cleaned_data
                return HttpResponseRedirect(reverse('order_view',
                                                    kwargs={'num': 1,
                                                            'lang': lang,
                                                            'curr': curr,
                                                            'country': fcd['country']}))
        else:
            form = Homepage_Form_Unique()
        return render_to_response('start.html', {'form': form,
                                                 'lang': lang,
                                                 'tech_info': tech_info,
                                                 'curr': curr,
                                                 'static_img':static_img_list,#Static_Img.objects.all(),#filter(static_img_text__lang=lang),
                                                 # static_img_text
                                                 'view': 'start'},
                                  context_instance=RequestContext(request))

    else:
        if request.method == 'POST':
            form = Homepage_Form(request.POST)
            if form.is_valid():
                fcd = form.cleaned_data
                return HttpResponseRedirect(reverse('order_view',
                                                    kwargs={'num': fcd['num'],
                                                            'lang': lang,
                                                            'country': fcd['country'],
                                                            'curr': curr}))
        else:
            form = Homepage_Form()
        return render_to_response('start.html', {'form': form,
                                                 'lang': lang,
                                                 'tech_info': tech_info,
                                                 'curr': curr,
                                                 'static_img':static_img_list,#Static_Img.objects.all(),
                                                 'view': 'start'},
                                  context_instance=RequestContext(request))


def order_view(request, num=1, lang='', curr='', country=''):
    tech_info = lang_id(lang)
    num = int(num)
    if request.method == 'POST':
        if Country.objects.get(country=country).is_it_your_country==True:
            form = Orders_Form_My_Country(request.POST,lang=lang,country=country)
        else:
            form = Orders_Form(request.POST,lang=lang,country=country)
        if form.is_valid():
            fcd = form.cleaned_data

            t_c = Transport_Company.objects.get(name=fcd['transport_company'])
            price = Currency.objects.get(curr_abbr=curr).curr_price
            s = num * price
            new_order = Orders(
                num=num,
                sum_price=s,
                curr=curr,
                fio=fcd['fio'],
                tel=fcd['tel'],
                country=Country.objects.get(country=country),
                city=fcd['city'],
                transport_company = fcd['transport_company'],     
                payment_method=fcd['payment_method'],
                additional_information=fcd['additional_information']
            )
            new_order.save()
            if Basic_Settings.objects.get(id=1).unique == True:
                unique = True
            else:
                unique = False
            form_homepage = Homepage_Form()
            return render_to_response(
                'start.html', {'thanks_for_buying': tech_info.thanks_for_buying,
                               'payment_method':fcd['payment_method'],
                               'tech_info': tech_info,
                               'num': num,
                               'lang': lang,
                               'curr': curr,
                               'view': 'start',
                               'sum_price': s, 'form': form_homepage},
                context_instance=RequestContext(request))
    else:
        if Country.objects.get(country=country).is_it_your_country==True:
            form = Orders_Form_My_Country(lang=lang,country=country)
        else:
            form = Orders_Form(lang=lang,country=country)      
    
    dict_order={'form': form,
                'tech_info': tech_info,
                'lang': lang,
                'curr': curr,
                'num': num,
                'transport_company_filter_country': Transport_Company.objects.filter(country__country=country),
                'transport_company_all': Transport_Company.objects.all(),
                'country': country,
                'view': 'order_view'}

    if type(form)==Orders_Form_My_Country:  
        dict_order['my_country']=True
    else:
        dict_order['my_country']=False

    return render_to_response('order.html',dict_order,
                              context_instance=RequestContext(request))


def shipping_and_payment(request, lang='', curr=''):
    tech_info = lang_id(lang)
    return render_to_response('shipping_and_payment.html',
                              {'tech_info': tech_info,
                               'lang': lang,
                               'curr': curr,
                               'view': 'shipping_and_payment'},
                              context_instance=RequestContext(request))


def contacts(request, lang='', curr=''):
    tech_info = lang_id(lang)
    all_is_right = ''

    if request.method == 'POST':
        form = Contacts(request.POST,lang=lang)
        if form.is_valid():
            fcd = form.cleaned_data
            new_letter = Contact(contact_subject=fcd['contact_subject'],
                                 name=fcd['name'],
                                 email=fcd['email'],
                                 text=fcd['text']
                                 )
            new_letter.save()
            all_is_right = Tech_Info.objects.get(id=1).contacts_thanks
            form = Contacts(lang=lang)
           # form_homepage=Homepage_Form()
           # return render_to_response('start.html',{'contacts_thanks':Tech_Info.objects.get(id=1).contacts_thanks,
            #                                        'form':form_homepage},
            # context_instance=RequestContext(request) )
    else:
        form = Contacts(lang=lang)
    return render_to_response('contacts.html', {'form': form,
                                                'all_is_right': all_is_right,
                                                'tech_info': tech_info,
                                                'lang': lang,
                                                'curr': curr,
                                                'view': 'contacts'},
                              context_instance=RequestContext(request))


def static_page(request, num, lang='', curr=''):
    tech_info = lang_id(lang)
    return render_to_response(
        'static_page.html', {'static_page': Static_Pages.objects.get(lang=Language.objects.get(lang_abbr=lang),
                                                                     num=num),
                             'tech_info': tech_info,
                             'lang': lang,
                             'curr': curr,
                             'view': 'static_page'},
        context_instance=RequestContext(request))
