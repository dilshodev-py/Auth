from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import ModelForm, ImageField

from apps.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return make_password(password)


class ProfileForm(ModelForm):
    photo = ImageField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'username', 'email', 'photo')
