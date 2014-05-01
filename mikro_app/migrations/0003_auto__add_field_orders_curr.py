# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Orders.curr'
        db.add_column(u'mikro_app_orders', 'curr',
                      self.gf('django.db.models.fields.CharField')(default=u'\u0432\u0430\u043b\u044e\u0442\u0430', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Orders.curr'
        db.delete_column(u'mikro_app_orders', 'curr')


    models = {
        u'mikro_app.contact': {
            'Meta': {'ordering': "['-date_time']", 'object_name': 'Contact'},
            'contact_subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_time': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_it_close': ('django.db.models.fields.CharField', [], {'default': "u'\\u041d\\u0435 \\u043f\\u0440\\u043e\\u0447\\u0438\\u0442\\u0430\\u043d\\u043e'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'mikro_app.country': {
            'Meta': {'object_name': 'Country'},
            'country': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'mikro_app.currency': {
            'Meta': {'object_name': 'Currency'},
            'curr_abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'curr_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'mikro_app.language': {
            'Meta': {'object_name': 'Language'},
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang_abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'})
        },
        u'mikro_app.orders': {
            'Meta': {'ordering': "['-date_time']", 'object_name': 'Orders'},
            'additional_information': ('redactor.fields.RedactorField', [], {'max_length': '10000'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'curr': ('django.db.models.fields.CharField', [], {'default': "u'\\u0432\\u0430\\u043b\\u044e\\u0442\\u0430'", 'max_length': '50'}),
            'date_time': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_it_close': ('django.db.models.fields.CharField', [], {'default': "u'\\u043d\\u043e\\u0432\\u044b\\u0439 \\u0437\\u0430\\u043a\\u0430\\u0437'", 'max_length': '100'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'sum_price': ('django.db.models.fields.FloatField', [], {}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'transport_company': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'mikro_app.static_img': {
            'Meta': {'ordering': "['num']", 'object_name': 'Static_Img'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'num': ('django.db.models.fields.IntegerField', [], {'default': '1', 'unique': 'True'}),
            'start': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mikro_app.Tech_Info']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'mikro_app.static_pages': {
            'Meta': {'ordering': "['num']", 'object_name': 'Static_Pages'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'text': ('redactor.fields.RedactorField', [], {'default': "u'This page is under construction'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'mikro_app.tech_info': {
            'Meta': {'object_name': 'Tech_Info'},
            'all_social_network_bool': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cod_is_impossible': ('redactor.fields.RedactorField', [], {'default': "u'\\u041e\\u043f\\u043b\\u0430\\u0442\\u0430 \\u043d\\u0430\\u043b\\u043e\\u0436\\u0435\\u043d\\u043d\\u044b\\u043c \\u043f\\u043b\\u0430\\u0442\\u0435\\u0436\\u0435\\u043c \\u043d\\u0435 \\u043e\\u0441\\u0443\\u0449\\u0435\\u0441\\u0442\\u0432\\u043b\\u044f\\u0435\\u0442\\u0441\\u044f'", 'max_length': '1000'}),
            'cod_is_possible': ('redactor.fields.RedactorField', [], {'default': "u'\\u0412\\u043e\\u0437\\u043c\\u043e\\u0436\\u043d\\u0430 \\u043e\\u043f\\u043b\\u0430\\u0442\\u0430 \\u043d\\u0430\\u043b\\u043e\\u0436\\u0435\\u043d\\u043d\\u044b\\u043c \\u043f\\u043b\\u0430\\u0442\\u0435\\u0436\\u0435\\u043c'", 'max_length': '1000'}),
            'contacts_text': ('redactor.fields.RedactorField', [], {'default': 'u\'\\u0442\\u0435\\u043a\\u0441\\u0442 \\u043d\\u0430 \\u0441\\u0442\\u0440\\u0430\\u043d\\u0438\\u0446\\u0435 "\\u041a\\u043e\\u043d\\u0442\\u0430\\u043a\\u0442\\u044b"\''}),
            'contacts_thanks': ('django.db.models.fields.CharField', [], {'default': "u'\\u0421\\u043f\\u0430\\u0441\\u0438\\u0431\\u043e \\u0437\\u0430 \\u0432\\u0430\\u0448\\u0435 \\u043f\\u0438\\u0441\\u044c\\u043c\\u043e'", 'max_length': '10000'}),
            'delivery_without_cod': ('django.db.models.fields.CharField', [], {'default': "u'\\u0421 \\u044d\\u0442\\u0438\\u043c \\u043f\\u0435\\u0440\\u0435\\u0432\\u043e\\u0437\\u0447\\u0438\\u043a\\u043e\\u043c \\u043e\\u043f\\u043b\\u0430\\u0442\\u0430                                \\u043d\\u0430\\u043b\\u043e\\u0436\\u0435\\u043d\\u043d\\u044b\\u043c \\u043f\\u043b\\u0430\\u0442\\u0435\\u0436\\u0435\\u043c \\u043d\\u0435 \\u043e\\u0441\\u0443\\u0449\\u0435\\u0441\\u0442\\u0432\\u043b\\u044f\\u0435\\u0442\\u0441\\u044f'", 'max_length': '1000'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "u'email@ukr.net'", 'max_length': '75', 'blank': 'True'}),
            'fb': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'fb_bool': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'homepage_text': ('redactor.fields.RedactorField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_additional_information': ('redactor.fields.RedactorField', [], {'default': "u'\\u0443\\u043a\\u0430\\u0436\\u0438\\u0442\\u0435 \\u043d\\u043e\\u043c\\u0435\\u0440 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0430,\\u0433\\u0434\\u0435 \\u0445\\u043e\\u0442\\u0435\\u043b\\u0438 \\u0431\\u044b \\u043f\\u043e\\u043b\\u0443\\u0447\\u0438\\u0442\\u044c \\u043f\\u043e\\u0441\\u044b\\u043b\\u043a\\u0443                              \\u0438\\u043b\\u0438 \\u0441\\u0432\\u043e\\u0439 \\u043f\\u043e\\u043b\\u043d\\u044b\\u0439 \\u0430\\u0434\\u0440\\u0435\\u0441, \\u0435\\u0441\\u043b\\u0438 \\u0432\\u044b  \\u0432\\u044b\\u0431\\u0440\\u0430\\u043b\\u0438 \\u043e\\u0442\\u043f\\u0440\\u0430\\u0432\\u043a\\u0443 \\u0423\\u043a\\u0440\\u043f\\u043e\\u0447\\u0442\\u043e\\u0439'", 'max_length': '1000'}),
            'info_cod_or_bankcard': ('redactor.fields.RedactorField', [], {'default': "u'\\u043d\\u0430\\u043b\\u043e\\u0436\\u0435\\u043d\\u043d\\u044b\\u0439 \\u043f\\u043b\\u0430\\u0442\\u0435\\u0436 \\u0423\\u043a\\u0440\\u043f\\u043e\\u0447\\u0442\\u043e\\u0439 \\u043d\\u0435 \\u043e\\u0441\\u0443\\u0449\\u0435\\u0441\\u0442\\u0432\\u043b\\u044f\\u0435\\u0442\\u0441\\u044f'", 'max_length': '1000'}),
            'label_additional_information': ('django.db.models.fields.CharField', [], {'default': "u'\\u0434\\u043e\\u043f\\u043e\\u043b\\u043d\\u0438\\u0442\\u0435\\u043b\\u044c\\u043d\\u0430\\u044f \\u0438\\u043d\\u0444\\u043e\\u0440\\u043c\\u0430\\u0446\\u0438\\u044f'", 'max_length': '10000'}),
            'label_button_contacts': ('django.db.models.fields.CharField', [], {'default': "u'\\u041a\\u043e\\u043d\\u0442\\u0430\\u043a\\u0442\\u044b'", 'max_length': '50'}),
            'label_button_contacts_in_page': ('django.db.models.fields.CharField', [], {'default': "u'\\u041e\\u0442\\u043f\\u0440\\u0430\\u0432\\u0438\\u0442\\u044c'", 'max_length': '50'}),
            'label_button_send': ('django.db.models.fields.CharField', [], {'default': "u'\\u041e\\u0442\\u043f\\u0440\\u0430\\u0432\\u0438\\u0442\\u044c'", 'max_length': '50'}),
            'label_button_shipping_and_payment': ('django.db.models.fields.CharField', [], {'default': "u'\\u0414\\u043e\\u0441\\u0442\\u0430\\u0432\\u043a\\u0430 \\u0438 \\u043e\\u043f\\u043b\\u0430\\u0442\\u0430'", 'max_length': '50'}),
            'label_buy_button': ('django.db.models.fields.CharField', [], {'default': "u'\\u0417\\u0430\\u043a\\u0430\\u0437\\u0430\\u0442\\u044c'", 'max_length': '50'}),
            'label_buy_num': ('django.db.models.fields.CharField', [], {'default': "u'\\u0423\\u043a\\u0430\\u0436\\u0438\\u0442\\u0435 \\u043a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e'", 'max_length': '50', 'blank': 'True'}),
            'label_city': ('django.db.models.fields.CharField', [], {'default': "u'\\u0433\\u043e\\u0440\\u043e\\u0434'", 'max_length': '100'}),
            'label_cod_or_bankcard': ('django.db.models.fields.CharField', [], {'default': "u'\\u0441\\u043f\\u043e\\u0441\\u043e\\u0431 \\u043e\\u043f\\u043b\\u0430\\u0442\\u044b'", 'max_length': '1000'}),
            'label_contacts_email': ('django.db.models.fields.CharField', [], {'default': "u'e-mail:'", 'max_length': '100'}),
            'label_contacts_name': ('django.db.models.fields.CharField', [], {'default': "u'\\u041f\\u0440\\u0435\\u0434\\u0441\\u0442\\u0432\\u0442\\u0435\\u0441\\u044c'", 'max_length': '100'}),
            'label_contacts_subject': ('django.db.models.fields.CharField', [], {'default': "u'\\u0422\\u0435\\u043c\\u0430'", 'max_length': '100'}),
            'label_contacts_text': ('django.db.models.fields.CharField', [], {'default': "u'\\u0422\\u0435\\u043a\\u0441\\u0442'", 'max_length': '10000'}),
            'label_fio': ('django.db.models.fields.CharField', [], {'default': "u'\\u0424\\u0418\\u041e'", 'max_length': '100'}),
            'label_tel': ('django.db.models.fields.CharField', [], {'default': "u'\\u0442\\u0435\\u043b\\u0435\\u0444\\u043e\\u043d'", 'max_length': '20'}),
            'label_transport_company': ('django.db.models.fields.CharField', [], {'default': "u'\\u0442\\u0440\\u0430\\u043d\\u0441\\u043f\\u043e\\u0440\\u0442\\u043d\\u0430\\u044f \\u043a\\u043e\\u043c\\u043f\\u0430\\u043d\\u0438\\u044f'", 'max_length': '1000'}),
            'label_url_offices': ('django.db.models.fields.CharField', [], {'default': "u'\\u041e\\u0444\\u0438\\u0441\\u044b'", 'max_length': '100'}),
            'label_url_shipping_and_payment': ('django.db.models.fields.CharField', [], {'default': "u'\\u0423\\u0441\\u043b\\u043e\\u0432\\u0438\\u044f \\u043e\\u043f\\u043b\\u0430\\u0442\\u044b \\u0438 \\u0434\\u043e\\u0441\\u0442\\u0430\\u0432\\u043a\\u0438'", 'max_length': '100'}),
            'lang': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mikro_app.Language']", 'blank': 'True'}),
            'logo': ('django.db.models.fields.CharField', [], {'default': "u'Kramar_mikro'", 'max_length': '50'}),
            'order_text': ('redactor.fields.RedactorField', [], {'default': 'u\'\\u0442\\u0435\\u043a\\u0441\\u0442 \\u043d\\u0430 \\u0441\\u0442\\u0440\\u0430\\u043d\\u0438\\u0446\\u0435 "\\u0411\\u043b\\u0430\\u043d\\u043a \\u0437\\u0430\\u043a\\u0430\\u0437\\u0430"\''}),
            'order_title': ('django.db.models.fields.CharField', [], {'default': "u'\\u0411\\u043b\\u0430\\u043d\\u043a \\u0437\\u0430\\u043a\\u0430\\u0437\\u0430'", 'max_length': '100'}),
            'shipping_and_payment_text': ('redactor.fields.RedactorField', [], {'default': 'u\'\\u0442\\u0435\\u043a\\u0441\\u0442 \\u043d\\u0430 \\u0441\\u0442\\u0440\\u0430\\u043d\\u0438\\u0446\\u0435 "\\u0414\\u043e\\u0441\\u0442\\u0430\\u0432\\u043a\\u0430 \\u0438 \\u041e\\u043f\\u043b\\u0430\\u0442\\u0430"\''}),
            'thanks_for_buying': ('django.db.models.fields.CharField', [], {'default': "u'\\u0421\\u043f\\u0430\\u0441\\u0438\\u0431\\u043e \\u0437\\u0430 \\u043f\\u043e\\u043a\\u0443\\u043f\\u043a\\u0443'", 'max_length': '50'}),
            'title_contacts': ('django.db.models.fields.CharField', [], {'default': "u'\\u041a\\u043e\\u043d\\u0442\\u0430\\u043a\\u0442\\u044b'", 'max_length': '100'}),
            'title_shipping_and_payment': ('django.db.models.fields.CharField', [], {'default': "u'\\u0414\\u043e\\u0441\\u0442\\u0430\\u0432\\u043a\\u0430 \\u0438 \\u043e\\u043f\\u043b\\u0430\\u0442\\u0430'", 'max_length': '100'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'vk': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'vk_bool': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'youtube': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'youtube_bool': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'mikro_app.transport_company': {
            'Meta': {'object_name': 'Transport_Company'},
            'cod': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url_offices': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'url_shipping_and_payment': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['mikro_app']