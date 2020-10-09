from django.contrib.auth.forms import UserCreationForm
from django import forms

# class SubmittableForm(Form):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(*self.fields, Submit('submit', 'Submit'))
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = User


    def save(self, commit=True):
        user = super().save(commit)
        return user
