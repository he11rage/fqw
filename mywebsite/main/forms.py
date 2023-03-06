from django.contrib.auth.forms import UserCreationForm
from .models import Services
from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput, Textarea, ChoiceField


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