from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField

UserModel = get_user_model()


class UserCreateForm(UserCreationForm):

    class Meta:
        model = UserModel
        # This means that you only want the username field from your User model.
        # For the rest of the fields (password1, password2, error_messages), you have a custom implementation.
        fields = ("email",)
        # This means that the class you want to use for username field is UsernameField Class,
        # if that makes sense.
        field_classes = {"email": UsernameField}
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }),
            'password': forms.TextInput(
                attrs={
                    'placeholder': 'Password',
                }),
        }


class UserEditForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
