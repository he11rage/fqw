from .models import Props
from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput

class PropsForm(ModelForm):
    class Meta:
        model = Props
        fields = ['surname', 'name', 'patronymic', 'phone', 'date']

        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "patronymic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            "phone": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Удобная дата звонка'
            }),
        }