from django import forms
from .models import Contact


class MessageForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'phone': forms.TextInput(attrs={
                "class": "tailwind-input col-span-6",
                "placeholder": 'شماره تلفن'}),
            'sub': forms.TextInput(attrs={
                "class": "tailwind-input col-span-6",
                "placeholder": 'عنوان'}),
            'text': forms.TextInput(attrs={
                "class": "tailwind-input col-span-12 h-24",
                "placeholder": 'متن دیدگاه '}),

        }
