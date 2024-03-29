from datetime import date

from django import forms
from django.contrib.auth.forms import (
    UserCreationForm as BaseUserCreationForm,
    UserChangeForm as BaseUserChangeForm,
)
from django.utils.html import strip_tags
from django.template.defaultfilters import linebreaksbr

from users.models import User


class UserCreationForm(BaseUserCreationForm):
    birthday = forms.DateField(
        label='Дата рождения',
        widget=forms.SelectDateWidget(
            years=[i for i in range(1900, date.today().year - 14)],
        )
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'birthday', )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = linebreaksbr(
            strip_tags(self.fields['password1'].help_text).replace('.', '.\n')
        )


class UserChangeForm(BaseUserChangeForm):
    birthday = forms.DateField(
        label='Дата рождения',
        widget=forms.SelectDateWidget(
            years=[i for i in range(1900, date.today().year)],
        )
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'birthday', )

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['password']
        self.fields['email'].initial = self.instance.email
        self.fields['username'].initial = self.instance.username
        self.fields['birthday'].initial = self.instance.birthday
