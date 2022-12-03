from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from the_forum.accounts.forms import UserCreateForm
from the_forum.articles.models import Article

''' 
1. index 
2. like_article 
3. dislike_article 
3. share_article 
4. comment_article 
'''
UserModel = get_user_model()


class HomeView(TemplateView):
    # TODO: should it redirect there
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        # TODO: should be with username
        user = UserModel.objects.filter(id=self.request.user.pk).get()
        context['username'] = user.get_username
        #     photo = Photo.objects.filter(pk=pk) \
        #         .get()

        # context['articles'] = UserModel.objects.filter.get()
        # context['profile'] = UserModel.objects\
        #     .prefetch_related('tagged_articles')\
        #     .filter(tagged_articles__user_profile=self.request.user)
        # TODO: how to connect the articles to the current user

        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login user')
        return super().dispatch(request, *args, **kwargs)


'''

def show_dashboard(request):
    profile = get_profile()
    # get all the photos of the tagged pets for the given user
    pet_photos = set(
                PetPhoto.objects
                .prefetch_related('tagged_pets')
                .filter(tagged_pets__user_profile=profile))
    context = {
        'pet_photos': pet_photos,

    }

    return render(request, 'dashboard.html', context)


def show_pet_photo_details(request, pk):
    pet_photo = PetPhoto.objects\
        .prefetch_related('tagged_pets')\
        .get(pk=pk)

    context = {
        'pet_photo': pet_photo,
    }

    return render(request, 'photo_details.html', context)


def like_pet_photo(request, pk):
    # like the photo with pk
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()

    return redirect('pet photo details', pk)
    
    
# we have created a CBV from the function above
class HomeView(RedirectToDashboard, TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context
        
        
class DashboardView(ListView):
    model = Game
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hide_additional_fields = False
        context['games'] = Game.objects.all()
        return context
'''