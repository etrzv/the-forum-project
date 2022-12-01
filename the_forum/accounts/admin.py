from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model

from the_forum.accounts.forms import UserEditForm, UserCreateForm
from the_forum.accounts.models import Profile

UserModel = get_user_model()

# https://stackoverflow.com/questions/73811593/add-fields-from-another-model-to-the-admin-site
@admin.register(UserModel)
# from django.contrib.auth.admin import UserAdmin was changed to suit the users' info
class UserAdmin(ModelAdmin):
    # form = UserEditForm
    form = UserCreateForm

    list_display = ('email', 'is_staff', 'is_superuser', 'is_active')  # what appears on the search bar above the users
    list_filter = ('is_staff', 'is_superuser', )    # filter on the right
    search_fields = ('email', )

    # for editing
    fieldsets = (
        (
            'Mandatory Information:',
            {
                'fields': (
                    'email',
                    'password1',
                    'password2',
                ),
            }),
        (
            'Important dates:',
            {
                'fields': (
                    'last_login',
                    'date_joined',
                ),
            },
        ),
        (
            'Permissions:',
            {
                'fields': (
                    'is_staff',
                    'is_superuser',
                ),
            }),
    )

    # for creating
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide', ),
                'fields': (
                    'email',
                    'password',
                    # 'password2',
                ),
            }),
    )

    def get_form(self, request, obj=None, **kwargs):
        """
        Return a Form class for use in the admin add view. This is used by
        add_view and change_view.
        """
        return super().get_form(request, obj, **kwargs)



