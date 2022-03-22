from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)

    def send_mail(self):
        pass