from django import forms
from django.forms.utils import ErrorDict

class LoginForm(forms.Form):
    SIGN_IN = 'sign-in'
    SIGN_UP = 'sign-up'
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.widgets.PasswordInput)
    password_confirm = forms.CharField(
        widget=forms.widgets.PasswordInput)
    name = forms.CharField()

    # ?? how about using decorator
    # @forms.Form.errors.getter
    @property
    def errors(self):
        errors = ErrorDict(super(forms.Form, self).errors)
        if not self.is_sign_up():
            errors.pop('password_confirm', None)
            errors.pop('name', None)
        return errors

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if self.is_sign_up():
            password = cleaned_data.get('password')
            password_confirm = cleaned_data.get('password_confirm')
            if password != password_confirm:
                self.add_error(
                    'password_confirm',
                    "passwords don't match")
        return cleaned_data

    def is_sign_in(self):
        return self.data.get(self.SIGN_IN) is not None

    def is_sign_up(self):
        return self.data.get(self.SIGN_UP) is not None
