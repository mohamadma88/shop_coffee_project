from django import forms
from .models import Contact


class ContactForm(forms.Form):
    phone = forms.CharField(max_length=5, label='phone')
    sub = forms.CharField(max_length=100, label='sub')
    text = forms.CharField(max_length=1000, label='text')

    def clean(self):
        phone = self.cleaned_data.get('phone')
        sub = self.cleaned_data.get('sub')
        text = self.cleaned_data.get('text')


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
