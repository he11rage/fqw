from django.db import models

# Create your models here.

class Props(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    text = models.CharField('Текст заявки', max_length=400)
    phone = models.CharField('Телефон', max_length=20)
    date = models.DateTimeField('Дата заявки')

    def __str__(self):
        return f'Заявка: {self.surname} {self.name} {self.patronymic}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'