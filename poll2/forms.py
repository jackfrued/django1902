import hashlib
import re

from django import forms
from django.core.exceptions import ValidationError

from poll2.models import User

USERNAME_PATTERN = re.compile(r'\w{6,20}')
TEL_PATTERN = re.compile(r'1[3-9]\d{9}')


def password_to_md5(password):
    """获取密码的MD5摘要"""
    return hashlib.md5(password.encode()).hexdigest()


def check_username(username):
    """验证用户名是否有效"""
    matcher = USERNAME_PATTERN.fullmatch(username)
    if not matcher:
        raise ValidationError('用户名由字母、数字、下划线构成且长度为6-20')
    return username


def check_password(password):
    if len(password) < 8:
        raise ValidationError('密码长度不应该小于8个字符')
    return password_to_md5(password)


class LoginForm(forms.Form):
    username = forms.CharField(min_length=6, max_length=20)
    password = forms.CharField(min_length=8, max_length=20)
    code = forms.CharField(min_length=4, max_length=4)

    def clean_username(self):
        return check_username(self.cleaned_data['username'])

    def clean_password(self):
        return check_password(self.cleaned_data['password'])


class UserForm(forms.ModelForm):
    password = forms.CharField(min_length=8, max_length=20,
                               widget=forms.PasswordInput, label='密码')

    def clean_username(self):
        return check_username(self.cleaned_data['username'])

    def clean_password(self):
        return check_password(self.cleaned_data['password'])

    def clean_tel(self):
        tel = self.cleaned_data['tel']
        matcher = TEL_PATTERN.fullmatch(tel)
        if not matcher:
            raise ValidationError('无效的手机号码')
        return tel

    class Meta:
        model = User
        exclude = ('no', )


class RegisterForm(UserForm):
    repassword = forms.CharField(min_length=8, max_length=20)
    code = forms.CharField(min_length=6, max_length=6)
    agreement = forms.BooleanField(required=True)

    def clean_repassword(self):
        password = self.cleaned_data['password']
        repassword = self.cleaned_data['repassword']
        if password != password_to_md5(repassword):
            raise ValidationError('密码和确认密码需要一致')
        return repassword
