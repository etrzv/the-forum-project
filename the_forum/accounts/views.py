from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from the_forum.accounts.forms import UserCreateForm

'''
UserModel = get_user_model()
1. SignInView(CreateView)
2. SignUpView(LoginView)
3. SingOutView(LogoutView)
4. UserDetailsView(DetailView)
5. UserEditView(UpdateView)
6. UserDeleteView(DeleteView)
'''

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('show index')

