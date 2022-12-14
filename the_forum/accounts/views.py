from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth import update_session_auth_hash
from django.views.generic import UpdateView, DetailView, CreateView, DeleteView

from the_forum.accounts.forms import UserCreateForm, UserEditForm, PasswordResetForm, UserProfileEditForm, \
    UserDeleteForm
from the_forum.accounts.models import Profile
from the_forum.articles.models import Article
from the_forum.common.forms import SearchArticleForm
from the_forum.common.models import ArticleBookmark

'''
When a request url matches a url in your urls.py file, django passes that request to the view you specified. 
The request can only be passed to callable functions. This is why when using class-based views, you use 
the as_view() method. The as_view() method returns a function that can be called.

This function then creates an instance of the view class and calls it's dispatch() method. The dispatch method 
then looks at the request and decides whether the GET or POST method of the view class should handle the request.
'''
UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    search_form = SearchArticleForm
    success_url = reverse_lazy('show index')

    # signing the user in after successful sign up
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.search_form
        return context

    #     def form_valid(self, form):
    #         form.instance.user = self.request.user
    #         return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     response = super().post(request, *args, **kwargs)
    #     login(request, self.object)
    #     return response


# LoginView -> form_class = AuthenticationForm -> username / password
class SignInView(LoginView):
    template_name = 'accounts/login-page.html'
    search_form = SearchArticleForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.search_form
        return context


class SignOutView(LogoutView):
    next_page = reverse_lazy('show index')
    search_form = SearchArticleForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.search_form
        return context


class UserDetailsView(DetailView):
    """
    Render a "detail" view of an object.
    By default, this is a model instance looked up from `self.queryset`, but the
    view will support display of *any* object by overriding `self.get_object()`.
    """

    template_name = 'accounts/profile-details-page.html'
    model = UserModel
    # instead of 'object_list' which is used in the html we can customise it
    context_object_name = 'profile'
    search_form = SearchArticleForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        #                                              self.object is a Profile
        articles = list(Article.objects.filter(user_id=self.object.pk))

        # Photo's field for likes is named `{NAME_OF_THIS_MODEL.lower()}_set`
        # using APIs we can access related objects

        bookmarked_articles = ArticleBookmark.objects.filter(user_id=self.object.pk)

        is_owner = self.request.user == self.object
        context.update({
            'articles': articles,
            'bookmarked_articles': bookmarked_articles,
            'is_owner': is_owner,
            'search_form': self.search_form,
        })

        return context


class UserEditView(LoginRequiredMixin, UpdateView):
    model = UserModel
    second_model = Profile
    template_name = 'accounts/profile-edit-page.html'

    form_class = UserEditForm
    second_form_class = UserProfileEditForm

    search_form = SearchArticleForm

    # TODO: edit with the form or use the model?
    # from - ModelFormMixin
    # Determine the URL to redirect to when the form is successfully validated.
    # Returns success_url by default

    # ProcessFormView
    """Handle GET requests: instantiate a blank version of the form."""

    """
    Handle POST requests: instantiate a form instance with the passed
    POST variables and then check if it's valid.
    """

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.model.objects.get(id=self.request.user.pk)
        profile = self.second_model.objects.get(user_id=user.pk)

        context.update({
            'form_class': self.form_class(instance=user),
            'second_form_class': self.second_form_class(instance=profile),
            'search_form': self.search_form,
        })

        return context

    def post(self, request, *args, **kwargs):
        user = self.model.objects.get(id=self.request.user.pk)
        profile = self.second_model.objects.get(user_id=user.pk)

        form = self.form_class(request.POST, instance=user)
        second_form = self.second_form_class(request.POST, instance=profile)

        if form.is_valid() and second_form.is_valid():
            form.save()
            second_form.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('edit user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('show index')
    form_class = UserDeleteForm
    search_form = SearchArticleForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.search_form
        return context


def change_password_view(request, pk):
    user = UserModel.objects.get(pk=pk)
    search_form = SearchArticleForm
    if request.method == 'POST':
        form = PasswordResetForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            # Now an important bit is to call update_session_auth_hash() after you save the form.
            # Otherwise, the user???s auth session will be invalidated and she/he will have to log in again.
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordResetForm(user)

    context = {
        'form': form,
        'search_form': search_form,
    }

    return render(request, 'accounts/profile-password-change.html', context)

