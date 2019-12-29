from django import forms
from django.shortcuts import redirect

from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['mail']

    def clean_email(self):
        """ For existing mail checking """
        mail = self.cleaned_data['mail']
        if Subscriber.objects.filter(mail=mail).exists():
            return False
        return mail