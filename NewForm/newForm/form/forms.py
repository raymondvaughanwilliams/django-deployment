from django import forms
from form.models import User
from django.core import validators

# def check_for_z(value):
#     if value[0] != 'z':
#         raise forms.ValidationError("Name has to start with z")

# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='Enter your email again')
#     text =forms.CharField(widget=forms.Textarea)

#     def clean(self):
#         all_clean_data =super().clean()
#         email = all_clean_data['email']
#         vmail =all_clean_data['verify_email']

#         if email != vmail:
#             raise forms.ValidationError("Emails dont match")
    

class NewUser(forms.ModelForm):
    class Meta:
        model =User
        fields ='__all__'


    # def clean_botcatcher(self):
    #     botcatcher =self.cleaned_data['botcatcher']
    #     if len(botcatcher)> 0:
    #         raise forms.ValidationError("A BOT!!")
    #     return botcatcher