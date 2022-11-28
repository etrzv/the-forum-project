from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from the_forum.accounts.forms import UserCreateForm


UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('show index')

    # signing the user in after successful sign up
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


# LoginView -> form_class = AuthenticationForm -> username / password
class SignInView(LoginView):
    template_name = 'accounts/login-page.html'
    # success_url = reverse_lazy('show index')


class SignOutView(LogoutView):
    next_page = reverse_lazy('show index')


class UserDetailsView(DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserEditView(UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('email', 'username')

    # TODO: edit with the form or use the model?
    def get_success_url(self):
        # return reverse_lazy('details user', kwargs={
        #     'pk': self.request.user.pk,
        # })
        return reverse_lazy('show index')


class UserDeleteView(DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('show index')
