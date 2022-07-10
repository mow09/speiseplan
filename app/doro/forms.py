# from django.forms import Form, ModelForm, BooleanField, CharField, TextField, EmailField
from django import forms
from users.models import Contact


class ContactForm(forms.ModelForm):
    privacy_place = forms.BooleanField(required=True)

    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'e_mail',
            'message',
            'place',
            'privacy_place'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Vorname',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Nachname',
            }),
            'e_mail': forms.EmailInput(attrs={
                'placeholder': 'E-Mail',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Nachricht',
            }),
            'privacy_place': forms.BooleanField(),
        }

# class ContactForm(forms.Form):
#     privacy_place = forms.BooleanField(required=True)
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;','class': 'form-control'}))
#     last_nameforms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
#     e_mail = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;'}))
#
#     message
#     place
#     privacy_place
#
#     class Meta:
#         model = Contact
#         fields = [
#             'first_name',
#             'last_name',
#             'e_mail',
#             'message',
#             'place',
#             'privacy_place'
#         ]

# from django.core.mail import send_mail
#
# if form.is_valid():
#     subject = form.cleaned_data['subject']
#     message = form.cleaned_data['message']
#     sender = form.cleaned_data['sender']
#     cc_myself = form.cleaned_data['cc_myself']
#
#     recipients = ['info@example.com']
#     if cc_myself:
#         recipients.append(sender)
#
#     send_mail(subject, message, sender, recipients)
#     return HttpResponseRedirect('/thanks/')
