from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment
from django.utils.safestring import mark_safe



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,
                                 help_text='Обязательное поле. Введите ваше имя.', label='Имя:')
    last_name = forms.CharField(max_length=30, required=False, help_text='Введите фамилию.', label='Фамилия:')
    email = forms.EmailField(max_length=254, required=True,
                             help_text='Обязательное поле.Введите действующий адрес электронной почты.',
                             label='E-mail:')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Пароль:', help_text=mark_safe(
                                '<ul>'
                                    '<li>Ваш пароль не должен содержать указанную вами личную информацию.</li>'
                                    '<li>Ваш пароль должен содержать как минимум 8 символов.</li>'
                                    '<li>Ваш пароль не может быть часто используемым паролем.</li>'
                                    '<li>Ваш пароль не может быть полностью числовым.</li>'
                                '</ul>'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )