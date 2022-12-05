import pyperclip as pyperclip
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from core.utils import apply_likes_count, apply_dislikes_count
from the_forum.accounts.forms import UserCreateForm
from the_forum.articles.models import Article
from the_forum.articles.utils import get_article_url
from the_forum.common.forms import ArticleCommentForm
from the_forum.common.models import ArticleLike, ArticleDislike

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
        articles = Article.objects.all()
        user = UserModel.objects.filter(id=self.request.user.pk).get()
        # user_like_articles = Article.objects.filter(pk=article.id, user_id=self.request.user.pk)
        likes = [apply_likes_count(article) for article in articles]
        dislikes = [apply_dislikes_count(article) for article in articles]

        context.update({
            'articles': articles,
            # 'likes': likes,
            # 'dislikes': dislikes,
        })

        #                      done in utils
        # context['articles'] = Article.objects.all()
        # context['articles_likes'] = [apply_likes_count(article) for article in Article.objects.all()]
        # context['articles_dislikes'] = [apply_dislikes_count(article) for article in Article.objects.all()]
        # context['username'] = user.get_username
        # context['articles'] = articles
        # context['likes'] = Article.objects.prefetch_related('like_set').all()

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

# def details_photo(request, pk):
#     photo = Photo.objects.filter(pk=pk) \
#         .get()
#
#     user_like_photos = Photo.objects.filter(pk=pk, user_id=request.user.pk)
#
#     context = {
#         'photo': photo,
#         'has_user_liked_photo': user_like_photos,
#         'likes_count': photo.photolike_set.count(),
#         'is_owner': request.user == photo.user,
#     }
#
#     return render(
#         request,
#         'photos/photo-details-page.html',
#         context,
#     )


#     photos = [apply_likes_count(photo) for photo in photos]
#     photos = [apply_user_liked_photo(photo) for photo in photos]
#     print(photos)
#     context = {
#         'photos': photos,
#         'comment_form': PhotoCommentForm(),
#         'search_form': search_form,
#     }
#
#     return render(
#         request,
#         'common/home-page.html',
#         context,
#     )


@login_required
def like_article(request, article_id):
    # articles have - id, slug, user_id fields
    #                                         accepts field names as kwargs
    user_liked_articles = ArticleLike.objects.filter(article_id=article_id, user_id=request.user.pk)

    if user_liked_articles:
        user_liked_articles.delete()
    else:
        ArticleLike.objects.create(article_id=article_id, user_id=request.user.pk)
    # A dictionary containing all available HTTP headers. Available headers depend on the client and server
    return redirect(get_article_url(request, article_id))


@login_required
def dislike_article(request, article_id):
    # articles have - id, slug, user_id fields
    #                                         accepts field names as kwargs
    user_disliked_articles = ArticleDislike.objects.filter(article_id=article_id, user_id=request.user.pk)

    if user_disliked_articles:
        user_disliked_articles.delete()
    else:
        ArticleDislike.objects.create(article_id=article_id, user_id=request.user.pk)
    # A dictionary containing all available HTTP headers. Available headers depend on the client and server
    return redirect(get_article_url(request, article_id))


@login_required
def share_article(request, article_id):
    pass
    # article_details_url = reverse('details article', kwargs={
    #     'pk': article_id
    # })
    # pyperclip.copy(article_details_url)
    # return redirect(get_article_url(request, article_id))


@login_required
def comment_article(request, article_id):
    article = Article.objects.filter(pk=article_id).get()

    form = ArticleCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=True)  # Does not persist to DB
        comment.article = article
        comment.save()

    context = {
        'form': form,
    }
    return render(request, 'articles/article-details-page.html', context)

    # return redirect(get_article_url(request, article_id))

# @login_required
# def share_article(request, article_id):
#     article_details_url = reverse('')


# @login_required
# def like_photo(request, photo_id):
#     user_liked_photos = PhotoLike.objects \
#         .filter(photo_id=photo_id, user_id=request.user.pk)
#
#     if user_liked_photos:
#         user_liked_photos.delete()
#     else:
#         PhotoLike.objects.create(
#             photo_id=photo_id,
#             user_id=request.user.pk,
#         )
#
#     return redirect(get_photo_url(request, photo_id))
#
# def get_photo_url(request, photo_id):
#     return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
#
#
#
# @login_required
# def comment_photo(request, photo_id):
#     photo = Photo.objects.filter(pk=photo_id) \
#         .get()
#
#     form = PhotoCommentForm(request.POST)
#
#     if form.is_valid():
#         comment = form.save(commit=False)  # Does not persist to DB
#         comment.photo = photo
#         comment.save()
#
#     return redirect('index')




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