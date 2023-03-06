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



