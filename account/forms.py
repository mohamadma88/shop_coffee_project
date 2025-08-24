from wsgiref.validate import validator
from django import forms
from account.models import Address
from .validator import validate_phone

class CreateAddress(forms.ModelForm):
    user = forms.IntegerField(required=False)

    class Meta:
        model = Address
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'fullname': forms.TextInput(
                attrs={'class': 'tailwind-input col-span-6', 'placeholder': 'نام و نام خانوادگی*'}),
            'address': forms.TextInput(attrs={'class': 'tailwind-input col-span-12', 'placeholder': 'آدرس*'}),
            'phone': forms.TextInput(attrs={'class': 'tailwind-input col-span-6', 'placeholder': 'شماره تلفن*'}),
            'postal_code': forms.TextInput(attrs={'class': 'tailwind-input col-span-6', 'placeholder': 'کد پستی*'}),
            'text': forms.TextInput(attrs={'class': 'tailwind-input col-span-6 h-24', 'placeholder': 'توضیحات اضافه'}),
        }


class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'appearance-none bg-transparent w-full py-3', 'placeholder': 'شماره تلفن '}))
    password = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'appearance-none bg-transparent w-full py-3', 'placeholder': 'رمز عبور'}))

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        validate_phone(phone)
        return phone


class RegisterForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'appearance-none bg-transparent w-full py-3',
                                                          'placeholder': 'شماره تلفن خود را وارد کنید . . . '}))

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        try:
            validate_phone(phone)
        except Exception as e:
            raise forms.ValidationError(str(e))
        return phone


class CheckOtpForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'appearance-none bg-transparent w-full py-3',
                                                         'placeholder': 'رمز عبور ارسال شده را وارد کنید . . . '}))
