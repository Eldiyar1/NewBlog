from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password_repeat = password
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("password_repeat"):
            raise forms.ValidationError("The password doesn't match!")

        del cleaned_data['password_repeat']
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)