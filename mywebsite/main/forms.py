from django.contrib.auth.forms import UserCreationForm
from .models import Services, Feedback
from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput, Textarea, ChoiceField, SelectDateWidget


class RegisterForm(UserCreationForm):
    pass


class ServicesForm(ModelForm):
    class Meta:
        model = Services
        fields = ['title', 'price', 'full_text', 'category']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название услуги'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Подробная информация'
            }),
            "category": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Категория'
            }),
        }

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['surname', 'name', 'patronymic', 'phone_number', 'feedback_text', 'date', 'time']

        widgets = {
            "surname": TextInput(attrs={
                'style': "border: none; border-bottom: 1px solid white; background-color: transparent;",
                'minlength': 4,
                'maxlength': 50,
                'required': '',
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "name": TextInput(attrs={
                'style': "border: none; border-bottom: 1px solid white; background-color: transparent;",
                'minlength': 4,
                'maxlength': 50,
                'required': '',
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "patronymic": TextInput(attrs={
                'style': "border: none; border-bottom: 1px solid white; background-color: transparent;",
                'minlength': 4,
                'maxlength': 50,
                'required': '',
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            "phone_number": TextInput(attrs={
                'style': "border: none; border-bottom: 1px solid white; background-color: transparent;",
                'minlength': 11,
                'maxlength': 11,
                'required': '',
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "feedback_text": Textarea(attrs={
                'style': "border: none; border-bottom: 1px solid white; background-color: transparent;",
                'class': 'form-control',
                'placeholder': 'Текст',
                'cols': 15, 'rows': 5
            }),
            "date": DateInput(attrs={
                'style': "border: none; border-bottom: 1px solid white; background-color: transparent;",
                'class': 'form-control'
            }),
            "time": TimeInput(attrs={
                'style': "border: none; border-bottom: 1px solid white; background-color: transparent;",
                'class': 'form-control'
            }),
        }

