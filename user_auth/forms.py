from django import forms
from user_auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    # passwordConfirm = forms.CharField(label='パスワード(確認)', required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
        )