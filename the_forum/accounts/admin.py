from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from the_forum.accounts.forms import UserEditForm, UserCreateForm, UserProfileEditForm
from the_forum.accounts.models import Profile

UserModel = get_user_model()

# https://stackoverflow.com/questions/73811593/add-fields-from-another-model-to-the-admin-site


# @admin.register(Profile)
class ProfileAdministration(admin.StackedInline):
    model = Profile


@admin.register(UserModel)
class UserAdministration(admin.ModelAdmin):
    add_form = UserCreateForm
    change_form = UserEditForm
    profile_change_form = UserProfileEditForm
    inlines = (ProfileAdministration, )

    list_display = ('email', 'is_staff', 'is_superuser', 'is_active')  # what appears on the search bar above the users
    list_filter = ('is_staff', 'is_superuser', )    # filter on the right
    search_fields = ('email', )

    fieldsets = (
        (
            'Mandatory Information:',
            {
                'fields': (
                    'email',
                ),
            }
        ),
        (
            'Important dates:',
            {
                'fields': (
                    'last_login',
                ),
            },
        ),
        (
            'Permissions:',
            {
                'fields': (
                    'is_staff',
                    'is_superuser',
                    'is_active',
                    'groups',
                    'user_permissions',
                ),
            }
        ),
    )

    add_fieldsets = (
        (
            'Mandatory Information:',
            {
                'classes': ('wide', ),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'first_name',
                    'last_name',
                    'username',
                ),
            }
         ),
        (
            'Permissions:',
            {
                'fields': (
                    'is_staff',
                    'is_superuser',
                    'is_active',
                    'groups',
                    'user_permissions',
                ),
            }
        ),
    )

    def get_form(self, request, obj=None, **kwargs):
        """
        Return a Form class for use in the admin add view. This is used by
        add_view and change_view.
        """
        if not obj:
            self.form = self.add_form
        else:
            self.form = self.change_form

        return super(UserAdministration, self).get_form(request, obj, **kwargs)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            fieldsets = self.add_fieldsets
            return fieldsets
        else:
            fieldsets = self.fieldsets
            return fieldsets
        # return super(UserAdministration, self).get_fieldsets(request, obj)
