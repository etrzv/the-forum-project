from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField, ReadOnlyPasswordHashField

from the_forum.accounts.models import Profile

UserModel = get_user_model()


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = UserModel
        fields = ('email', )
        field_classes = {'email': auth_forms.UsernameField}

    def save(self, commit=True):
        user = super().save(commit=commit)
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        profile = Profile(
            first_name=first_name,
            last_name=last_name,
            user=user,
        )
        if commit:
            profile.save()
        return user


class UserEditForm(UserChangeForm):
    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserModel
        fields = ['email', 'password', 'is_active']


'''    
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
'''


