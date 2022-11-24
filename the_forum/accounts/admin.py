from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model

from the_forum.accounts.forms import UserEditForm, UserCreateForm
from the_forum.accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
# from django.contrib.auth.admin import UserAdmin was changed to suit the users' info
class UserAdmin(ModelAdmin):
    # list_display = ('email', 'password',)
    fieldsets = (
        (
            'Mandatory Information:',
            {
                'fields': (
                    'email',
                    'password',
                ),
            }),
        (
            'Important dates',
            {
                'fields': (
                    'last_login',
                    'date_joined',
                ),
            },
        ),
    )


'''    form = UserEditForm
    add_form = UserCreateForm
    list_filter = ()
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'password',
                ),
            }),

        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            'Important dates',
            {
                'fields': (
                    'last_login',
                    'date_joined',
                ),
            },
        ),
    )

    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)'''



