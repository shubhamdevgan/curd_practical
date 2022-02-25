from django import forms
from .models import UserModel
from django.conf import settings
from .utlis import compress_image


class UserCreationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password', 'confirm_password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError(
                {'confirm_password':
                 ["Password and Confirm Password must be same.", ]}
            )

    def save(self, commit=True, *args, **kwargs):
        user_obj = super().save()
        user_obj.set_password(user_obj.password)
        user_obj.save()
        return user_obj


class ProfileFillUpForm(forms.ModelForm):

    class Meta:
        model = UserModel
        exclude = ('username', 'email', 'password',
                   'is_active', 'is_superuser', 'is_staff', 'last_login')

    def clean_profile_image(self):
        profile_image = self.cleaned_data.get('profile_image')
        if profile_image.size > settings.MAX_IMAGE_UPLOAD:
            compressed_profile_image = compress_image(profile_image)
            return compressed_profile_image
        return profile_image
