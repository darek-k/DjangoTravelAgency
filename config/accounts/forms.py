from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



# class SignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ['username', 'first_name']
#
#     def save(self, commit=True):
#         user = super().save(commit)
#         return user

# class SubmittableForm(Form):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(*self.fields, Submit('submit', 'Submit'))
