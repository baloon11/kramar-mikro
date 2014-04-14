# coding: utf-8
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','mikro_app.views.start',name='start'), 
    url(r'^order/(?P<num>\d+)/$','mikro_app.views.order_view',name='order_view'), 
   # url(r'^order/$','mikro_app.views.order_view',name='order_view'), 


    #url(r'^confirmation/(?P<num>\d+)/(?P<s>\d+)/(?P<fio>\w+)/(?P<tel>\w+)/(?P<city>\w+)/(?P<transport_company>\w+)/(?P<cod_or_bankcard>\w+)/(?P<additional_information>\w+)/$',
     #   'mikro_app.views.confirmation_save',name='confirmation_save'), 

    url(r'^shipping_and_payment/$','mikro_app.views.shipping_and_payment',name='shipping_and_payment'), 
    url(r'^contacts/$','mikro_app.views.contacts',name='contacts'), 
    url(r'^static_page/(?P<num>\d+)/$','mikro_app.views.static_page',name='static_page'),


    url(r'^redactor/', include('redactor.urls')),
        
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),    
    
                       )
                                             
if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()


                       
