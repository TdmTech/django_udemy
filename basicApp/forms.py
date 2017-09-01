from django import forms


class FormName(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField()
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)



