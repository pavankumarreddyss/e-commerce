from django import forms
class ContactForm(forms.Form):
    contact_name=forms.CharField(label='Enter your name:',required=True)
    contact_email=forms.EmailField(label='Enter your Email id:',required=True)
    content=forms.CharField(label='enter your message:',required=True,widget=forms.Textarea)