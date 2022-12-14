from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField, ReadOnlyPasswordHashField, \
    PasswordChangeForm
from django.core.exceptions import ValidationError

from the_forum.accounts.models import Profile

UserModel = get_user_model()


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    # TODO: added
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    # class UserCreateForm(auth_forms.UserCreationForm):
    #     class Meta:
    #         model = UserModel
    #         fields = ('username', 'email')
    #         field_classes = {
    #             'username': auth_forms.UsernameField,
    #         }

    class Meta:
        model = UserModel
        fields = ('email', )
        # is a dictionary of model field names mapped to a form field class.
        # field_classes = {'email': auth_forms.UsernameField}

    # TODO: added
    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError("Passwords don't match")
    #     return password2

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=commit)
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        username = self.cleaned_data['username']
        # TODO: added
        # user.set_password(self.cleaned_data["password1"])
        profile = Profile(
            first_name=first_name,
            last_name=last_name,
            username=username,
            user=user,
        )

        if commit:
            profile.save()

        return user


class UserEditForm(UserChangeForm):
    # TODO: Changed for the admin site
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserModel
        # TODO: changed
        fields = ('email', )
        # exclude = ('password', )
        field_classes = {
            'email': auth_forms.UsernameField,

        }

    # def clean_password(self):
    #     # Regardless of what the user provides, return the initial value.
    #     # This is done here, rather than on the field, because the
    #     # field does not have access to the initial value
    #     return self.initial["password"]


class UserProfileEditForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', )

    def save(self, commit=True):
        self.instance.save()
        return self.instance


class PasswordResetForm(PasswordChangeForm):
    class Meta:
        model = UserModel


class UserDeleteForm(forms.ModelForm):
    def save(self, commit=True):
        # articles should remain after account deletion TODO: account author: Deleted
        self.instance.delete()
        return self.instance

    class Meta:
        model = UserModel
        fields = ()
