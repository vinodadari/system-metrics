from django import forms
from .models import Subscriber
from django.shortcuts import redirect
class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['mail']

    def clean_email(self):
        mail = self.cleaned_data['mail']
        if Subscriber.objects.filter(mail=mail).exists():
            return False
        return mail