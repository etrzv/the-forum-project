from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import update_session_auth_hash
from the_forum.accounts.forms import UserCreateForm, UserEditForm, PasswordResetForm, UserProfileForm
from the_forum.articles.models import Article

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
    success_url = reverse_lazy('show index')

    # signing the user in after successful sign up
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    #     def form_valid(self, form):
    #         form.instance.user = self.request.user
    #         return super().form_valid(form)


# LoginView -> form_class = AuthenticationForm -> username / password
class SignInView(LoginView):
    template_name = 'accounts/login-page.html'
    # success_url = reverse_lazy('show index')


class SignOutView(LogoutView):
    next_page = reverse_lazy('show index')


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        #                                              self.object is a Profile
        articles = list(Article.objects.filter(user_id=self.object.pk))
        user = UserModel.objects.filter(id=self.request.user.pk).get()
        first_name = user.get_first_name()
        context.update({
            'articles': articles,
            'user': user,
            'first_name': first_name,

        })

        return context


# model = Profile
#     template_name = 'main/../../templates/accounts/profile_details.html'
#     context_object_name = 'profile'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         #                               self.object is a Profile
#         pets = list(Pet.objects.filter(user_id=self.object.user_id))
#
#         pet_photos = PetPhoto.objects \
#             .filter(tagged_pets__in=pets) \
#             .distinct()
#
#         # distinct gives us just the unique values
#         total_likes_count = sum(pp.likes for pp in pet_photos)
#         total_pet_photos_count = len(pet_photos)
#
#         # update merges 2 dictionaries
#         context.update({
#             'total_likes_count': total_likes_count,
#             'total_pet_photos_count': total_pet_photos_count,
#             'is_owner': self.object.user_id == self.request.user.id,
#             'pets': pets,
#         })
#
#         return context


class UserEditView(UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('email', 'is_active', )
    # form_class = UserEditForm

    # TODO: edit with the form or use the model?
    # from - ModelFormMixin
    # Determine the URL to redirect to when the form is successfully validated.
    # Returns success_url by default
    def get_success_url(self):
        return reverse_lazy('edit user', kwargs={
            'pk': self.request.user.pk,
        })

    def get_context_data(self, *args, **kwargs):
        # user = UserModel.objects.filter(id=self.request.user.pk).get()
        user_profile = UserProfileForm(instance=self.request.user)  # / self.request.user.pk
        user_form = UserEditForm(instance=self.request.user.pk)
        # user_profile_form = UserProfileForm(instance=self.request.user.pk)

        context = super().get_context_data(**kwargs)
        context.update({
            # 'user': user.get_profile,
            'user_profile': user_profile,
            'user_form': user_form,
            # 'user_profile_form': user_profile_form,
        })
        return context


class UserDeleteView(DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('show index')


def article_details(request, slug):
    article = Article.objects.get(slug=slug)
    #     # path('article/<slug:slug>/', include([
    #     # = articles/article/1-witcher-3-ending/
    return render(request, 'articles/article-edit-page.html', {'article': article})


''' 

def edit_pet(request, pk):
    return pet_action(request, EditPetForm, 'profile details', Pet.objects.get(pk=pk), 'main/pet_edit.html')


def delete_pet(request, pk):
    return pet_action(request, DeletePetForm, 'profile details', Pet.objects.get(pk=pk), 'main/pet_delete.html')

'''


def change_password_view(request, pk):
    user = UserModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = PasswordResetForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            # Now an important bit is to call update_session_auth_hash() after you save the form.
            # Otherwise, the user’s auth session will be invalidated and she/he will have to log in again.
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordResetForm(user)

    context = {
        'form': form,
    }

    return render(request, 'accounts/profile-password-change.html', context)


# class Location(models.Model):
#     description = model.CharField(max_length=40)
#     address1 = model.CharField(max_length=40)
#     # ..... (and so on)
#     tel = model.CharField(max_length=12)

# class InformationRequest(models.Model):
#     source = models.ForeignKey(Location)
#     request_date = Models.DateField(default=datetime.now())
#     # ..... (and so on)

# >>> loc = Location()
# >>> loc.tel = "123"
# >>> loc.save()
# >>> info = InformationRequest()
# >>> info.source = loc
# >>> info.save()


# Fetching:

# >>> info.source.tel ==> Child.user.first_name
# '123'

# class InformationRequest(models.Model):
#     source = models.ForeignKey(Location, related_name="information_requests")
#     request_date = Models.DateField(default=datetime.now())
#     # ..... (and so on)
#
#     def contact_tel(self):
#         return self.source.tel

# >>> info.contact_tel()
# '123'

# OR

# class InformationRequest(models.Model):
#     source = models.ForeignKey(Location, related_name="information_requests")
#     request_date = Models.DateField(default=datetime.now())
#     # ..... (and so on)
#
#     @property
#     def contact_tel(self):
#         return self.source.tel

# >>> info.contact_tel
# '123'

'''
Model: 
UserProfile = child user = OneToOneField

UserForm():
    model = User
    fields = ()

UserProfileForm():
    model = UserProfile 

def edit_profile(self, request):
    user_form = UserForm(instance=request.user)
    user_profile_form = UserProfileForm(instance=request.user.userprofile)
'''