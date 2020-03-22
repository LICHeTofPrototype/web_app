from django import forms

class LoginForms(forms.From):
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