from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class LoginForms(forms.Form):
    email = forms.EmailField(
        label='Eメール',
        max_length = 255,
    )
    password = forms.CharField(
        label="パスワード",
        widget = forms.PasswordInput(render_value=True),
    )

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        try:
            user = User.objrects.get(email=email)
        except ObjectDoesNotExist:
            raise forms.ValidationError('ユーザーが登録されていません')
        if not user.check_password(password):
            raise forms.ValidationError("正しいパスワードを入力してください")