from django.contrib.auth.forms import UserCreationForm


# class SubmittableForm(Form):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(*self.fields, Submit('submit', 'Submit'))


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    def save(self, commit=True):
        user = super().save(commit)
        return user






