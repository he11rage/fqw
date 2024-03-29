# Generated by Django 4.1.2 on 2022-11-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Props',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(default='Не указано', max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(default='Не указано', max_length=50, verbose_name='Имя')),
                ('patronymic', models.CharField(default='Не указано', max_length=50, verbose_name='Отчество')),
                ('phone', models.CharField(default='Не указано', max_length=20, verbose_name='Телефон')),
                ('date', models.DateTimeField(verbose_name='Дата заявки')),
            ],
        ),
    ]
