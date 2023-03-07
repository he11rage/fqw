from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Services(models.Model):
    title = models.CharField('Заглавие', max_length=50)
    price = models.CharField('Стоимость', max_length=50)
    full_text = models.TextField('Об услуге')
    category = models.CharField('Категория', max_length=50)

    def __str__(self):
        return f' Услуга: {self.category}: {self.title} '

    def get_absolute_url(self):
        return f'/settings/{self.id}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Feedback(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    phone_number = models.CharField('Телефон', max_length=12)
    feedback_text = models.TextField('Подробности')
    date = models.DateField('Дата звонка')
    time = models.TimeField('Время звонка', default=0)

    def __str__(self):
        return f'Заявка: {self.surname} {self.name} {self.patronymic}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
