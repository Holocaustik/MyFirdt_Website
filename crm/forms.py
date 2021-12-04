from django import forms


class OrderForms(forms.Form):
    name = forms.CharField(label='Введите имя', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Введите телефон', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
