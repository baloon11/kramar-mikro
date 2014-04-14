# coding: utf-8
from django.db import models
from redactor.fields import RedactorField
def list_payment_method():
    payment_method_list=[(u'банковская карта',u'банковская карта'),
                        (u'наложенный платеж',u'наложенный платеж') ]
    return payment_method_list 


def list_is_it_close():
    is_it_close_list=[(u'новый заказ',u'новый заказ'),
                      (u'в обработке',u'в обработке'),
                     (u'обработанный',u'обработанный') ]
    return is_it_close_list 


def list_transport_company():
    list_name=list()    
    all_comp=Transport_Company.objects.count()
    if all_comp>0:
        for n in xrange(1,all_comp+1):
            comp_name=Transport_Company.objects.get(id=n).name
            list_name.append( (unicode(comp_name),unicode(comp_name)) ) #unicode(comp_name)
        return list_name
    else:
        list_name.append( (u'свяжитесь с менеджером по поводу доставки',
                         u'свяжитесь с менеджером по поводу доставки') )
        return list_name

def contact_is_it_close():
    is_it_close_list=[(u'не прочитано',u'не прочитано'),
                      (u'прочитано',u'прочитано') ]
    return is_it_close_list 


class Tech_Info(models.Model):                           
    price=models.IntegerField(verbose_name=u'цена',default=0)
    unique=models.BooleanField(default=True,
                                    verbose_name=u'Товар продается в единичном экземпляре \
                                    (галочка-да-в единичном)',
                                     help_text=u'Если товар уникальный,\
                                     то на главной страние не будет выдаваться окно для количества товара')
#  ____________________________"Бланк заказа"_____________________   
    order_title=models.CharField(verbose_name=u'Заголовок в браузере на странице "Бланк заказа"',max_length=100,default=u'Бланк заказа')
    order_text=RedactorField(verbose_name=u'текст на странице "Бланк заказа"',default=u'текст на странице "Бланк заказа"')
    label_fio=models.CharField(verbose_name=u'ФИО',max_length=100,
                               help_text='надпись слева от формы',
                               default=u'ФИО') 
    
    label_tel=models.CharField(verbose_name=u'телефон',max_length=20,
                               help_text='надпись слева от формы',
                               default=u'телефон')
    
    label_city=models.CharField(verbose_name=u'город',max_length=100,
                               help_text='надпись слева от формы',
                               default=u'город')
    
    label_transport_company=models.CharField(verbose_name=u'транспортная компания',
                               max_length=1000,
                               help_text='надпись слева от формы', 
                               default=u'транспортная компания')

    label_cod_or_bankcard=models.CharField(verbose_name=u'наложенный платеж или перевод на банковскую карту',
                               max_length=1000,
                               help_text=' надпись слева от формы',
                               default=u'наложенный платеж или перевод на банковскую карту')
    #label_bankcard=models.CharField(
     #                         verbose_name=u'перевод на банковскую карту',
     #                         max_length=1000,
     #                         help_text=' надпись слева от формы',
     #                         default=u'перевод на банковскую карту')
    label_additional_information=models.CharField(
                              max_length=10000,
                              verbose_name=u'дополнительная информация',
                              help_text='надпись слева от формы',
                              default=u'дополнительная информация')

    info_cod_or_bankcard=RedactorField(
                               verbose_name=u'доп. информация к способу оплаты',
                               max_length=1000,
                               help_text=' надпись снизу формы',
                               default=u'наложенный платеж Укрпочтой не осуществляется')

    info_additional_information=RedactorField(
                              verbose_name=u'дополнительная информация в помощь покупателю',
                              max_length=1000,
                              help_text=' надпись снизу от формы\
                              (указывается напротив поля "дополнительная информация")',
                              default=u'укажите номер склада,где хотели бы получить посылку\
                              или свой полный адрес, если вы  выбрали отправку Укрпочтой') 
    

    delivery_without_cod=models.CharField(                              
                               verbose_name=u'С этим перевозчиком оплата \
                               наложенным платежем не осуществляется',
                               max_length=1000,
                               help_text=' Надпись в форме при ошибке заполнения. \
                               Появляется, если покупатель выбрал наложенный платеж и \
                               компанию, через которую отправка наложенным платежем не осуществляется',
                               default=u'С этим перевозчиком оплата \
                               наложенным платежем не осуществляется')

    label_url_offices=models.CharField(verbose_name=u'Как отображается ссылка на страницу с офисами перевозчика',
                                       max_length=100,
                                       default=u'Офисы')

    label_url_shipping_and_payment=models.CharField(verbose_name=u'Как отображается ссылка на страницу с условиями оплаты и доставка перевозчика',
                                          max_length=100,
                                          default=u'Условия оплаты и доставки')

    cod_is_possible=RedactorField(verbose_name=u'Возможна оплата наложенным платежем',
                                     max_length=1000,
                                     help_text=u'Колонка со всеми возможными перевозчиками.\
                                                Подпись под каждым перевозчиком',
                                     default=u'Возможна оплата наложенным платежем')
    
    cod_is_impossible=RedactorField(verbose_name=u'Оплата наложенным платежем не осуществляется',
                                     max_length=1000,
                                     help_text='Колонка со всеми возможными перевозчиками.\
                                                Подпись под каждым перевозчиком',
                                     default=u'Оплата наложенным платежем не осуществляется')
    
    label_button_send=models.CharField(
                              verbose_name=u'надпись в кнопке "Отправить"',
                              max_length=50,
                              default=u'Отправить')
    

#______________________________Главная страница_______________________________
    logo=models.CharField(verbose_name=u'логотип(надпись)',
                          max_length=50,
                          default=u'Kramar_mikro')
    homepage_text=RedactorField(verbose_name=u'текст на Главной странице')

    #logo_img=models.
    thanks_for_buying=models.CharField(verbose_name=u'Спасибо за покупку(надпись)',
                          max_length=50,
                          default=u'Спасибо за покупку')

    email=models.EmailField(verbose_name=u'email магазина',default=u'email@ukr.net',blank=True)
    
    social_network_title=models.CharField(verbose_name=u'Шапка социальных сетей',
                                          max_length=100,
                                          blank=True,
                                          default=u'Также вы можете найти нас')

    all_social_network_bool= models.BooleanField(default=True,
                                                 blank=True, 
                                                 verbose_name=u'Должна ли быть видна вся\
                                                 колонка "Соц сети" (галочка-должна)')
    
    vk=models.URLField(verbose_name=u'ссылка на сообщество Вконтакте',blank=True)
    vk_bool= models.BooleanField(default=True,blank=True, 
                                 verbose_name=u'Должна ли быть видна\
                                 кнопка Вконтакте (галочка-должна)')
     
    fb=models.URLField(verbose_name=u'ссылка на сообщество Facebook',blank=True)
    fb_bool= models.BooleanField(default=True, blank=True,
                                 verbose_name=u'Должна ли быть видна\
                                 кнопка Facebook (галочка-должна)')
    
    youtube=models.URLField(verbose_name=u'ссылка на канал youtube',blank=True)
    youtube_bool= models.BooleanField(default=True, blank=True,
                                    verbose_name=u'Должна ли быть видна \
                                    кнопка Youtube (галочка-должна)')

    label_buy_num=models.CharField(
                              verbose_name=u'Укажите количество',
                              max_length=50,
                              default=u'Укажите количество',
                              blank=True)

    label_buy_button=models.CharField(
                              verbose_name=u'надпись в кнопке "Заказать"',
                              max_length=50,
                              default=u'Заказать')

    label_button_contacts=models.CharField(
                              verbose_name=u'надпись в кнопке "Контакты"',
                              max_length=50,
                              default=u'Контакты')     

    label_button_shipping_and_payment=models.CharField(
                              verbose_name=u'надпись в кнопке "Доставка и оплата"',
                              max_length=50,
                              default=u'Доставка и оплата')



#____________________________________Контакты_______________________________
    title_contacts=models.CharField(verbose_name=u'Заголовок в браузере',max_length=100,default=u'Контакты')
    contacts_text=RedactorField(verbose_name=u'текст на странице "Контакты"',default=u'текст на странице "Контакты"')

    label_contacts_subject=models.CharField(verbose_name=u'Тема',max_length=100,default=u'Тема')

    label_contacts_name=models.CharField(verbose_name=u'Имя',max_length=100,default=u'Предствтесь')

    label_contacts_email=models.CharField(verbose_name=u'e-mail:',max_length=100,default=u'e-mail:')

    label_contacts_text=models.CharField(verbose_name=u'Текст',max_length=10000,default=u'Текст')
    contacts_thanks=models.CharField(verbose_name=u'сообщение пользователю, что его письмо получено',
                                     max_length=10000,default=u'Спасибо за ваше письмо')
    label_button_contacts_in_page=models.CharField(
                              verbose_name=u'надпись в кнопке "Отправить письмо"',
                              max_length=50,
                              default=u'Отправить')


#________________________________Доставка и оплата__________________________
    title_shipping_and_payment=models.CharField(verbose_name=u'Заголовок в браузере',max_length=100,default=u'Доставка и оплата')

    shipping_and_payment_text=RedactorField(verbose_name=u'текст на странице "Доставка и Оплата"',
                                            default=u'текст на странице "Доставка и Оплата"')

    def __unicode__(self):
        return u'техническая информация' 

    class Meta:
        verbose_name_plural = "Раздел настрорек сайта" 
        verbose_name = "\"техническая информация\""


class Transport_Company(models.Model):
    name=models.CharField(verbose_name=u'Название транспортной компании',
                          max_length=50)
    money=models.IntegerField(verbose_name=u'стоимость доставки(не наложенным платежем)',
                              default=0)
    cod= models.BooleanField(default=True,
                                    verbose_name=u'осуществляет ли эта компания\
                                                   доставку наложенным платежем')
    
    url_offices=models.URLField(verbose_name=u'ссылка на страницу со списком отделений')
    
    url_shipping_and_payment=models.URLField(verbose_name=u'ссылка на страницу c\
                                                            условиями доставки и оплаты')
    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name_plural = "Транспортные компании" 
        verbose_name = "\"Транспортная компания\" " 
                                                            

class Orders(models.Model):
    date_time = models.DateField(verbose_name=u'дата заказа',auto_now=True)      
    fio=models.CharField(verbose_name=u'ФИО',max_length=100) 
    tel=models.CharField(verbose_name=u'телефон',max_length=20)
    city=models.CharField(verbose_name=u'город',max_length=50)                                                              
    transport_company=models.CharField(verbose_name=u'транспортная компания',
                                       choices=list_transport_company(),
                                       max_length=1000)
    sum_price=models.FloatField(verbose_name=u'общая сумма заказа')
    num=models.IntegerField(verbose_name=u'количество заказанного товара')

    payment_method=models.CharField(verbose_name=u'Метод оплаты', 

                                    max_length=1000,
                                    choices=list_payment_method())  
    
    additional_information=RedactorField(
                              max_length=10000,
                              verbose_name=u'Дополнительная информация')
    
    is_it_close=models.CharField(verbose_name=u'статус заказа', 
                                 choices=list_is_it_close(),
                                 max_length=100,
                                 default=u'новый заказ')
    
    def __unicode__(self):
        return '%s %s' % (self.date_time,self.is_it_close) 

    class Meta:
        verbose_name_plural = "Заказы" 
        verbose_name = "\"заказ\" "
        ordering = ["-date_time"] 

class Static_Img(models.Model):
    img = models.ImageField(verbose_name=u'Фото', upload_to='media/', help_text=u'Помещается 5 уменьшеных изображений в строку')    
    title = models.CharField(u'подпись к фото', max_length=1000) 
    num=models.IntegerField(verbose_name=u'Порядковый номер фото при выводе',default=1,unique=True)

    start=models.ForeignKey(Tech_Info,verbose_name=u'Присоединение фото к разделу технической информации')

    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ["num"]
        verbose_name_plural = "Фотографии"
        verbose_name = "photo"

class Contact(models.Model): 
    contact_subject = models.CharField(max_length=100, verbose_name=u'Тема письма ')
    date_time = models.DateField(verbose_name=u'Когда пришло письмо ' ,auto_now=True)          
    name = models.CharField(max_length=100, verbose_name=u'Имя',blank=True)
    email = models.EmailField(verbose_name=u'e-mail ',blank=True)
    text = models.TextField(verbose_name=u'Текст ')
    is_it_close=models.CharField(verbose_name=u'Прочитано ли письмо', 
                                 choices=contact_is_it_close(),
                                 max_length=100,
                                 default=u'Не прочитано')


    class Meta: 
        verbose_name = ('Contact')
        verbose_name_plural = ('Contacts')
        ordering = ["-date_time"]        
    def __unicode__(self): 
        return '%s %s %s' % (self.date_time,self.contact_subject,self.is_it_close)