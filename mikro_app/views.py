# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from mikro_app.models import Tech_Info,Transport_Company,Orders,Contact
from mikro_app.forms import Homepage_Form,Orders_Form,Contacts
from django.template import RequestContext 
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def start(request):
    if Tech_Info.objects.get(id=1).unique==True:
        return render_to_response('start.html',context_instance=RequestContext(request) 
                                    )
    else:
        if request.method == 'POST':    
            form=Homepage_Form(request.POST)
            if form.is_valid():
                fcd = form.cleaned_data
                return HttpResponseRedirect (reverse('order_view', kwargs={'num':fcd['num']}))
        else:
            form=Homepage_Form()
        return render_to_response('start.html',{'form':form},
                                          context_instance=RequestContext(request) )

def order_view(request,num=1):
    num=int(num)
    if request.method == 'POST':    
        form=Orders_Form(request.POST)
        if form.is_valid():
            fcd = form.cleaned_data

            t_c=Transport_Company.objects.get(name=fcd['transport_company'])
            price=Tech_Info.objects.get(id=1).price            
            if fcd['cod_or_bankcard']==u'наложенный платеж':                     
                s=num*price        
                cod=True
            else:
                money=t_c.money 
                s=num*price+money
                cod=False
            new_order= Orders (
                          num=num,
                          sum_price=s,
                          fio=fcd['fio'],
                          tel=fcd['tel'],
                          city=fcd['city'],
                          transport_company=fcd['transport_company'],
                          payment_method=fcd['cod_or_bankcard'],
                          additional_information=fcd['additional_information']
                        )
            new_order.save()
            if Tech_Info.objects.get(id=1).unique==True:
                unique=True
            else:
                unique=False
            form_homepage=Homepage_Form()
            return render_to_response('start.html',{'thanks_for_buying':Tech_Info.objects.get(id=1).thanks_for_buying,
                                                     'sum_price':s,'cod':cod,'form':form_homepage}, 
                                       context_instance=RequestContext(request) )               
    else:
        form=Orders_Form()
    return render_to_response('order.html',{'form':form}, 
                                       context_instance=RequestContext(request) )

def shipping_and_payment(request):
    return render_to_response('shipping_and_payment.html', 
                              context_instance=RequestContext(request) )

def contacts(request):
    all_is_right = ''
    if request.method == 'POST':    
        form=Contacts(request.POST)
        if form.is_valid():
            fcd = form.cleaned_data
            new_letter=Contact(contact_subject=fcd['contact_subject'],
                               name=fcd['name'] ,
                               email=fcd['email'] ,
                               text=fcd['text']
                               )
            new_letter.save()
            all_is_right = Tech_Info.objects.get(id=1).contacts_thanks            
            form=Contacts()
           # form_homepage=Homepage_Form()
           # return render_to_response('start.html',{'contacts_thanks':Tech_Info.objects.get(id=1).contacts_thanks,
            #                                        'form':form_homepage}, 
            #                           context_instance=RequestContext(request) )
    else:
        form=Contacts()
    return render_to_response('contacts.html',{'form':form,'all_is_right': all_is_right}, 
                                       context_instance=RequestContext(request) )