# coding: utf-8
from django.db import models
from redactor.fields import RedactorField
from django.db.models.signals import post_init, post_save, post_delete
from django.dispatch import receiver

class Basic_Settings(models.Model):
    title=models.CharField(verbose_name=u'Описание', max_length=300,default=u'Базовые настройки')                           
    unique=models.BooleanField(default=True,
                                    verbose_name=u'товар продается в ед.экземпляре',
                                     help_text=u'Если товар уникальный,\
                                     то на главной страние не будет выдаваться окно для количества товара')

    email=models.EmailField(verbose_name=u'email',default=u'email@ukr.net',blank=True)
    
    def __unicode__(self):
        return '%s %s' % (self.unique,self.email) 
                                                
    class Meta:
        verbose_name_plural = "Базовые настройки"
        verbose_name = "'Базовые настройки'"


class Social_Network (models.Model):
    title=models.CharField(verbose_name=u'Название ресурса', max_length=300)
    link_soc=models.URLField(verbose_name=u'ссылка на ресурс',blank=True)
    bool_soc= models.BooleanField(default=True,blank=True, 
                                 verbose_name=u'вкл.иконку') 
    img_soc= models.ImageField(verbose_name=u'Иконка',
                               upload_to='media/',
                               blank=True,
                               help_text=u'Рекомендованный размер 48х48')    

    def __unicode__(self):
        return '%s' % self.title
                                                
    class Meta:
        verbose_name_plural = "Соц. сети и доп. ресурсы"
        verbose_name = "ресурс"


class Tech_Info(models.Model):                           
    lang=models.ForeignKey('Language',blank=True)
#  ____________________________"Бланк заказа"_____________________   
    order_title=models.CharField(verbose_name=u'Заголовок в браузере на странице "Бланк заказа"',max_length=100,default=u'Бланк заказа')
    button_popup_in_page=models.CharField(verbose_name=u'Надпись в кнопке, по которому запускается всплывающее окно',
                                          max_length=100, 
                                          default=u'all transport companies') 

    label_in_head_popup=models.CharField(verbose_name=u'Надпись в шапке всплывающего окна',
                                          max_length=100, 
                                          default=u'all transport companies')    

    button_popup_close=models.CharField(verbose_name=u'Надпись в кнопке всплывающего окна',
                                          max_length=100, 
                                          default=u'Close')
    order_text=RedactorField(verbose_name=u'текст на странице "Бланк заказа"',
                             default=u'текст на странице "Бланк заказа"')
    
    please_correct_errors=models.CharField(verbose_name=u'Текст"Пожалуйста, исправьте ошибки"',max_length=200,
                               help_text='надпись сверху формы, используется для форм "Бланк заказа" и "Контакты"',
                               default=u'Пожалуйста, исправьте ошибки') 
    
    label_fio=models.CharField(verbose_name=u'ФИО',max_length=100,
                               help_text='надпись слева от формы',
                               default=u'ФИО') 
    error_fio=models.CharField(verbose_name=u'ошибка при пустом поле "ФИО" ',max_length=100,
                               help_text=u'появляется на странице "Бланк заказа" при незаполненном поле "ФИО" ',
                               default=u'обязательное поле') 

    
    label_tel=models.CharField(verbose_name=u'телефон',max_length=20, 
                               help_text='надпись слева от формы',
                               default=u'телефон')
    error_tel=models.CharField(verbose_name=u'ошибка при пустом поле "Тел"',max_length=100,
                               help_text=u'появляется на странице "Бланк заказа" при незаполненном поле "Тел" ',
                               default=u'обязательное поле') 

    
    label_city=models.CharField(verbose_name=u'город',max_length=100,
                               help_text='надпись слева от формы',
                               default=u'город')
    error_city=models.CharField(verbose_name=u'ошибка при пустом поле "Город"',max_length=100,
                               help_text=u'появляется на странице "Бланк заказа" при незаполненном поле "Город" ',
                               default=u'обязательное поле') 
    
    label_transport_company=models.CharField(verbose_name=u'транспортная компания',
                               max_length=1000,
                               help_text='надпись слева от формы', 
                               default=u'транспортная компания')

    error_transport_company=models.CharField(verbose_name=u'ошибка при пустом поле "Транспортная компания"',max_length=100,
                               help_text=u'появляется на странице "Бланк заказа" при незаполненном поле "Транспортная компания" ',
                               default=u'обязательное поле') 


    label_payment_method=models.CharField(verbose_name=u'Способ оплаты',
                               max_length=1000,
                               help_text=' надпись слева от формы',
                               default=u'способ оплаты')

    error_payment_method=models.CharField(verbose_name=u'ошибка при пустом поле "Способ оплаты"',max_length=100,
                               help_text=u'появляется на странице "Бланк заказа" при незаполненном поле "Способ оплаты" ',
                               default=u'обязательное поле') 

    label_additional_information=models.CharField(
                              max_length=10000,
                              verbose_name=u'Дополнительная информация',
                              help_text='надпись слева от формы',
                              default=u'Дополнительная информация')

    error_additional_information=models.CharField(verbose_name=u'ошибка при пустом поле "Дополнительная информация"',max_length=100,
                               help_text=u'появляется на странице "Бланк заказа" при незаполненном поле "Дополнительная информация" ',
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
    

    delivery_without_cod=RedactorField(                              
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

    thanks_for_buying=models.CharField(verbose_name=u'Спасибо за покупку(надпись)',
                                       max_length=50,
                                       default=u'Спасибо за покупку')

    label_sum=models.CharField(verbose_name=u'Сумма без учета доставки (надпись)',
                               max_length=200,
                               default=u'Сумма без учета доставки')
    label_curr=models.CharField(verbose_name=u'Валюта (надпись)',
                               max_length=100,
                               default=u'Валюта')

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
    error_contacts_text=models.CharField(verbose_name=u'ошибка при пустом поле "Текст"',max_length=100, 
                               help_text=u'появляется на странице "Контакты" при незаполненном поле "Текст" ',
                               default=u'обязательное поле') 


    label_contacts_subject=models.CharField(verbose_name=u'Тема',max_length=100,default=u'Тема')
    error_contacts_subject=models.CharField(verbose_name=u'ошибка при пустом поле "Тема"',max_length=100,
                               help_text=u'появляется на странице "Контакты" при незаполненном поле "Тема" ',
                               default=u'обязательное поле') 



    label_contacts_name=models.CharField(verbose_name=u'Имя',max_length=100,default=u'Представтесь')
    error_contacts_name=models.CharField(verbose_name=u'ошибка при пустом поле "Имя"',max_length=100,
                               help_text=u'появляется на странице "Контакты" при незаполненном поле "Имя" ',
                               default=u'обязательное поле') 

    label_contacts_email=models.CharField(verbose_name=u'e-mail:',max_length=100,default=u'e-mail:')
    error_contacts_email=models.CharField(verbose_name=u'ошибка при пустом поле "e-mail"',max_length=100,
                               help_text=u'появляется на странице "Контакты" при незаполненном поле "e-mail" ',
                               default=u'обязательное поле') 

    error_contacts_email_value=models.CharField(verbose_name=u'ошибка при неправильно заполненном поле "e-mail"',max_length=100,
                               help_text=u'появляется на странице "Контакты" при  неправильно заполненном поле "e-mail" ',
                               default=u'Проверте правильность введенного e-mail') 


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
                          max_length=50,unique=True)
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
    transport_company=models.CharField(verbose_name=u'транспортная компания',max_length=1000)
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
   # title = models.CharField(u'подпись к фото', max_length=1000) 
    num=models.IntegerField(verbose_name=u'Порядковый номер фото при выводе',default=1,unique=True)

   # start=models.ManyToManyField(Tech_Info,verbose_name=u'Присоединение фото к разделу технической информации')

    def __unicode__(self):
        return u'фото № %s'% str(self.num)
    class Meta:
        ordering = ['num']
        verbose_name = "фото"
        verbose_name_plural = "Фотографии"

#---------------------------------------------
class Static_Img_Text(models.Model):
    text = models.CharField(u'подпись к фото', max_length=1000,default=u'text') 
    img = models.ForeignKey(Static_Img, verbose_name=u'к какому фото относится',related_name='text_for_img')
    lang= models.CharField(verbose_name=u'язык описания',max_length=3)    

    def __unicode__(self):
        return ' %s %s' % (self.text,self.lang)

    class Meta:
        ordering = ['id']
        verbose_name = " подпись под фото"
        verbose_name_plural = "Подписи под фотографиями"

#--------------------------------------------

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
    lang=models.ForeignKey('Language')
    num=models.IntegerField(verbose_name=u'Порядковый номер страницы в списке')
    

    def __unicode__(self):
        return '%s %s%s' % (self.title,u'порядковый номер ',self.num)
    class Meta:
        ordering = ["num"]
        verbose_name_plural = "статические страницы"
        verbose_name = "'статическая страница'"

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