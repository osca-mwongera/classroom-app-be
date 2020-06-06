from django.contrib.auth.models import User
from .models import Profile

from django import forms

from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Required')
    last_name = forms.CharField(max_length=30, help_text='Required')
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(),
                             help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class LoginForm(UserForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')


def check_phone_number(self):
    phone_number = self['phone_number']
    safaricom_phone_number = ('25470', '25471', '25472', '254757', '254758', '254759', '254790', '254790', '254791', '254792')

    if any([phone_number.startswith(number) for number in safaricom_phone_number]) is False:
        raise forms.ValidationError("Please input your number beginning with the country code. It must be a "
                                    "Safaricom number")
    return phone_number


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # self.fields['avatar'].widget = forms.ImageField(required=False)
        # self.fields['gender'].widget = forms.ChoiceField(required=False)
        self.fields['phone_number'] = forms.CharField(
            required=True, help_text="please input a safaricom number beginning with the country code but"
                                     " do not include the '+' sign")
        # validators=check_phone_number(self) Its bringing up an error
        self.fields['alt_number'] = forms.CharField(required=False)
        self.fields['address'] = forms.CharField(required=False)
        self.fields['zip_code'] = forms.CharField(required=False)
        self.fields['town'] = forms.CharField(required=False)
        self.fields['region'] = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = (
            # 'avatar',
            # 'gender',
            'phone_number',
            'alt_phone',
            'address',
            'zip_code',
            'town',
            'region'
        )

    # def check_phone_number(self):
    #     phone_number = self.cleaned_data['phone_number']
    #     safaricom_phone_number = (
    #         '25470', '25471', '25472', '254757', '254758', '254759', '254790', '254790', '254791', '254792'
    #     )
    #
    #     # if any([phone_number.startswith(number) for number in safaricom_phone_number]) is False:
    #     #     raise forms.ValidationError("Please input your number beginning with the country code. It must be a "
    #     #                                 "Safaricom number")
    #     # return phone_number
    #
    #     # if not phone_number.startswith(tuple(safaricom_phone_number)):
    #     #     raise forms.ValidationError("Please input your number beginning with the country code."
    #     #                                 " It must be a Safaricom number")
    #
    #     if not phone_number[:6] in safaricom_phone_number:
    #         raise forms.ValidationError(
    #             "Please input your number beginning with the country code. It must be a Safaricom number"
    #         )
    #     return phone_number
