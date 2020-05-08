from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
                               attrs={'class':"uk-input",
                                      'type':"text",
                                      'placeholder':"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(
                               attrs={'class':"uk-input",
                                      'type':"password",
                                      'placeholder':"Password"}))

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
                               attrs={'class':"uk-input",
                                      'type':"text",
                                      'placeholder':"Username"}))

    email = forms.CharField(widget=forms.TextInput(
                               attrs={'class':"uk-input",
                                      'type':"email",
                                      'placeholder':"email@example.com"}))

    password1 = forms.CharField(widget=forms.PasswordInput(
                               attrs={'class':"uk-input",
                                      'type':"password",
                                      'placeholder':"Password"}))

    password2 = forms.CharField(widget=forms.PasswordInput(
                               attrs={'class':"uk-input",
                                      'type':"password",
                                      'placeholder':"Repeat your Password"}))
