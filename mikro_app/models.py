# coding: utf-8
from django.db import models
from redactor.fields import RedactorField
from django.db.models.signals import post_init, post_save, post_delete
from django.dispatch import receiver



class Tech_Info(models.Model):                           
    lang=models.ForeignKey('Language',blank=True)
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
    error_fio=models.CharField(verbose_name=u'ошибка при пустом поле "ФИО" ',max_length=100,
                               help_text=u'появляется на странице "Бланк заказа" при назаполненном поле "ФИО" ',
                               default=u'обязательное поле') 

    
    label_tel=models.CharField(verbose_name=u'телефон',max_length=20,
                               help_text='надпись слева от формы',
                               default=u'телефон')
    error_tel=models.CharField(verbose_name=u'ошибка при пустом поле "Тел"',max_length=100,
                               help_text=u'появляется на странице "Бланк заказа" при назаполненном поле "Тел" ',
                               default=u'обязательное поле') 

    
    label_city=models.CharField(verbose_name=u'город',max_length=100,
                               help_text='надпись слева от формы',
                               default=u'город')
    error_city=models.CharField(verbose_name=u'ошибка при пустом поле "Город"',max_length=100,
                               help_text=u'появляется на странице "Бланк заказа" при назаполненном поле "Город" ',
                               default=u'обязательное поле') 
    
    label_transport_company=models.CharField(verbose_name=u'транспортная компания',
                               max_length=1000,
                               help_text='надпись слева от формы', 
                               default=u'транспортная компания')

    error_transport_company=models.CharField(verbose_name=u'ошибка при пустом поле "Транспортная компания"',max_length=100,
                               help_text=u'появляется на странице "Бланк заказа" при назаполненном поле "Транспортная компания" ',
                               default=u'обязательное поле') 


    label_payment_method=models.CharField(verbose_name=u'Способ оплаты',
                               max_length=1000,
                               help_text=' надпись слева от формы',
                               default=u'способ оплаты')

    error_payment_method=models.CharField(verbose_name=u'ошибка при пустом поле "Способ оплаты"',max_length=100,
                               help_text=u'появляется на странице "Бланк заказа" при назаполненном поле "Способ оплаты" ',
                               default=u'обязательное поле') 

    label_additional_information=models.CharField(
                              max_length=10000,
                              verbose_name=u'Дополнительная информация',
                              help_text='надпись слева от формы',
                              default=u'Дополнительная информация')

    error_additional_information=models.CharField(verbose_name=u'ошибка при пустом поле "Дополнительная информация"',max_length=100,
                               help_text=u'появляется на странице "Бланк заказа" при назаполненном поле "Дополнительная информация" ',
                               default=u'обязательное поле') 


    info_payment_method=RedactorField(
                               verbose_name=u'доп. информация к способу оплаты',
                               max_length=1000,blank=True,
                               help_text=' надпись снизу формы',
                               default=u'наложенный платеж Укрпочтой не осуществляется')

    info_additional_information=RedactorField(
                              verbose_name=u'дополнительная информация в помощь покупателю',
                              max_length=1000,blank=True,
                              help_text=' надпись снизу от формы\
                              (указывается  внизу поля "дополнительная информация")',
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
    cod_text =models.CharField(verbose_name=u'наложенный платеж',
                                          max_length=100,
                                          help_text=u'надпись в выпадающем меню в форме заказа',
                                          default=u'наложенный платеж')
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

    label_sum=models.CharField(verbose_name=u'Сумма без учета доставки (надпись)',
                               max_length=200,
                               default=u'Сумма без учета доставки')
    label_curr=models.CharField(verbose_name=u'Валюта (надпись)',
                               max_length=100,
                               default=u'Валюта')

    email=models.EmailField(verbose_name=u'email магазина',default=u'email@ukr.net',blank=True)
    

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
        return u'техническая информация для языка '+'%s' % self.lang.lang_abbr

    class Meta:
        verbose_name_plural = "Раздел настрорек для разных языков " 
        


class Transport_Company(models.Model):
    name=models.CharField(verbose_name=u'Название транспортной компании',
                          max_length=50)
    cod= models.BooleanField(default=True,
                                    verbose_name=u'осуществляет ли эта компания\
                                                   доставку наложенным платежем')
    
    url_offices=models.URLField(verbose_name=u'ссылка на страницу со списком отделений',blank=True)
    
    url_shipping_and_payment=models.URLField(verbose_name=u'ссылка на страницу c\
                                                            условиями доставки и оплаты',blank=True)
    country=models.ManyToManyField('Country') 

    def __unicode__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name_plural = "Транспортные компании" 
        verbose_name = "\"Транспортная компания\" " 
                                                            

class Orders(models.Model):
    date_time = models.DateField(verbose_name=u'дата заказа',auto_now=True)      
    fio=models.CharField(verbose_name=u'ФИО',max_length=100) 
    tel=models.CharField(verbose_name=u'телефон',max_length=20)
    country=models.ForeignKey('Country',verbose_name=u'Страна')
    city=models.CharField(verbose_name=u'город',max_length=50)                                                              
    transport_company=models.ForeignKey(Transport_Company,verbose_name=u'транспортная компания',max_length=1000)
    payment_method=models.CharField(verbose_name=u'метод оплаты',max_length=1000)
    sum_price=models.FloatField(verbose_name=u'общая сумма заказа')
    curr=models.CharField(verbose_name=u'Валюта',max_length=50,default=u'валюта')  
    
    num=models.IntegerField(verbose_name=u'количество заказанного товара')
    
    additional_information=RedactorField(
                              max_length=10000,
                              verbose_name=u'Дополнительная информация')
    
    is_it_close=models.CharField(verbose_name=u'статус заказа', 
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

    start=models.ManyToManyField(Tech_Info,verbose_name=u'Присоединение фото к разделу технической информации')

    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['num']
        verbose_name = "фото"
        verbose_name_plural = "Фотографии"
        

class Contact(models.Model): 
    contact_subject = models.CharField(max_length=100, verbose_name=u'Тема письма ')
    date_time = models.DateField(verbose_name=u'Когда пришло письмо ' ,auto_now=True)          
    name = models.CharField(max_length=100, verbose_name=u'Имя',blank=True)
    email = models.EmailField(verbose_name=u'e-mail ',blank=True)
    text = models.TextField(verbose_name=u'Текст ')
    is_it_close=models.CharField(verbose_name=u'Прочитано ли письмо',
                                 max_length=100,
                                 default=u'Не прочитано')
        

    class Meta: 
        verbose_name = 'письмо'
        verbose_name_plural = "Письма от покупателей"
        ordering = ["-date_time"]        
    def __unicode__(self): 
        return '%s %s %s' % (self.date_time,self.contact_subject,self.is_it_close)

class Static_Pages(models.Model):
    title = models.CharField(u'Title', max_length=1000,blank=True) 
    text = RedactorField(verbose_name=u'Текст на странице',default=u'This page is under construction')
    num=models.IntegerField(verbose_name=u'Порядковый номер страницы в списке',unique=True)
    def __unicode__(self):
        return '%s %s' % (self.title,self.num)
    class Meta:
        ordering = ["num"]
        verbose_name_plural = "статические страницы"
        

class Language(models.Model):
    lang_abbr= models.CharField(u'двух(трех)буквенная аббревиатура языка',max_length=3,unique=True) 
    default=models.BooleanField(default=False,
                                verbose_name=u'язык по умолчанию')
                                    
    def __unicode__(self):
        if self.default==True:
            def_ault=u'Этот язык установлен для сайта по умолчанию'
        else:
            def_ault=u''
        return '%s %s' % (self.lang_abbr,def_ault)
    class Meta:
        verbose_name_plural = "Языки"

class Currency (models.Model):
    curr_abbr= models.CharField(u'название валюты',max_length=100,unique=True) 
    default=models.BooleanField(default=False,
                                verbose_name=u'валюта по умолчанию')
    curr_price=models.FloatField(verbose_name=u'цена в этой валюте',default=0)

                                    
    def __unicode__(self):
        if self.default==True:
            def_ault=u'Эта валюта установлена по умолчанию'
        else:
            def_ault=u''
        return '%s %s %s' % (def_ault,self.curr_price,self.curr_abbr)
    class Meta:
        verbose_name_plural = "Валюты"

class Country(models.Model):
    country=models.CharField(u'Страна',max_length=200,unique=True)
    is_it_your_country=models.BooleanField(default=False,
                                            verbose_name=u'осуществляестся ли в этой стране\
                                                           пересылка наложенным платежем',
                                            help_text='Если эта ваша страна проживания,то скорее всего,\
                                                       внутри нее(через местные транспортные компании)\
                                                       возможна пересылка наложенным платежем')

    def __unicode__(self):
        return '%s ' % self.country
    class Meta:
        verbose_name_plural = "страны"

class PaymentMethod(models.Model):
    payment_method=models.CharField(verbose_name=u'Метод оплаты', 
                                    max_length=1000,default=u'Метод оплаты',unique=True)  

    def __unicode__(self):
        return '%s ' % self.payment_method
    class Meta:
        verbose_name_plural = "Методы оплаты"

        


        
