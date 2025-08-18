from django import forms
from .models import Ticket, TicketReply


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'message']

        widgets = {
            'subject': forms.TextInput(attrs={
                "class": "tailwind-input col-span-6",
                "placeholder": 'عنوان'}),
            'message': forms.TextInput(attrs={
                "class": "tailwind-input col-span-12 h-24",
                "placeholder": 'متن'}),
        }

class TicketStatusForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['status']



class TicketReplyForm(forms.ModelForm):
    class Meta:
        model = TicketReply
        fields = ['message']
