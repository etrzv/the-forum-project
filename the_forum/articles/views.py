from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView

from core.utils import apply_likes_count, apply_dislikes_count
from the_forum.accounts.models import Profile
from the_forum.articles.forms import ArticleCreateForm, ArticleEditForm, ArticleDeleteForm
from the_forum.articles.models import Article
from the_forum.common.forms import ArticleCommentForm
from the_forum.common.models import ArticleComment

# Create your views here.

# The GET method, which was used in the example earlier, appends name/value pairs to the URL. Unfortunately,
# the length of a URL is limited, so this method only works if there are only a few parameters.
# The URL could be truncated if the form uses a large number of parameters, or if the parameters contain large amounts
# of data. Also, parameters passed on the URL are visible in the address field of the browser not the best place for
# a password to be displayed.

# The alternative to the GET method is the POST method. This method packages the name/value pairs inside the body
# of the HTTP request, which makes for a cleaner URL and imposes no size limitations on the forms output.
# It is also more secure.

# WORKS:
# @login_required
# def add_article(request):
#     # GET = view without change
#     if request.method == 'GET':
#         form = ArticleCreateForm()
#     else:
#         # POST = view and change
#         form = ArticleCreateForm(request.POST)
#         if form.is_valid():
#             article = form.save(commit=False)
#             article.user = request.user
#             article.save()
#             return redirect('show index')
#         #     pet = form.save(commit=False)
#         #     pet.user = request.user
#         #     pet.save()
#         #     return redirect('details user', pk=request.user.pk)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'articles/article-add-page.html', context)


UserModel = get_user_model()


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/article-add-page.html'
    form_class = ArticleCreateForm  # used in Django Class Based to depict the Form to be used in the view
    success_url = reverse_lazy('show index')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class ArticleEditView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'articles/article-edit-page.html'
    form_class = ArticleEditForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # TODO: check
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('edit article', kwargs={'slug': self.object.id})


'''    
def get_queryset(self):
        # This method is called by the default implementation of get_object() and
        # may not be called if get_object() is overridden.
        obj = get_object_or_404(
            Article,
            article_slug=self.kwargs['article_slug'])
        return obj
    
        # obj = get_object_or_404(Post, category__slug=self.kwargs['category_slug'],slug=self.kwargs['post_slug'] )
        # return obj
    
'''


# def edit_article(request, username, article_slug):
#     article = Article.objects.filter(slug=article_slug).get()

    # # if not is_owner(request, article):
    # #     return redirect('details pet', username=username, pet_slug=pet_slug)
    #
    # if request.method == 'GET':
    #     form = ArticleEditForm(instance=article)
    # else:
    #     form = ArticleEditForm(request.POST, instance=article)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('show index', username=username, article_slug=article_slug)
    #
    # context = {
    #     'form': form,
    #     'article_slug': article_slug,
    #     'username': username,
    # }
    #
    # return render(
    #     request,
    #     'articles/article-edit-page.html',
    #     context,
    # )


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
class ArticleDetailsView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'articles/article-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = Article.objects.get(id=self.object.pk)
        likes = [apply_likes_count(article)]
        dislikes = [apply_dislikes_count(article)]
        # user_likes_articles = Article.objects.filter(pk=self.object.pk, user_id=self.request.user.pk)
        user = UserModel.objects.get(id=self.request.user.pk)
        profile = Profile.objects.get(user_id=self.request.user.pk)
        comments = ArticleComment.objects.filter(article_id=article.id)
        comment_form = ArticleCommentForm
        context.update({
            'article': article,
            'likes': likes,
            'dislikes': dislikes,
            'is_owner': article.user == self.request.user,
            # 'has_user_liked_photo': user_likes_articles,
            'user': user,
            'profile': profile,
            'comments': comments,
            'comment_form': comment_form,
        })

        return context


# def article_details(request, slug):
#     article = Article.objects.get(slug=slug)
#     # path('article/<slug:slug>/', include([
#     # = articles/article/1-witcher-3-ending/
#
#     # comments = article.objects.filter(id=slug)
#     context = {
#         'article': article,
#         # 'comments': comments,
#     }
#     return render(request, 'articles/article-details-page.html', context)


class ArticleDeleteView(LoginRequiredMixin, DetailView):
    template_name = 'articles/article-delete-page.html'
    model = Article
    success_url = reverse_lazy('show index')
    form_class = ArticleDeleteForm


'''
class PetPhotoDetailsView(LoginRequiredMixin, DetailView):
    model = PetPhoto
    template_name = 'main/photo_details.html'
    context_object_name = 'pet_photo'
    
    def get_queryset(self):
        return super()\
            .get_queryset()\
            .prefetch_related('tagged_pets')

    def get_context_data(self, **kwargs):
        # in order for us to hide the edit / delete buttons under a picture that is not ours
        context = super().get_context_data()

        # we need to know the owner of the photo, so we can add / take functionality
        context['is_owner'] = self.object.user == self.request.user

        return context


# we make sure that only a logged user can use this functionality
class CreatePetPhotoView(LoginRequiredMixin, CreateView):
    model = PetPhoto
    template_name = 'main/photo_create.html'
    fields = ('photo', 'description', 'tagged_pets')

    success_url = reverse_lazy('dashboard')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditPetPhotoView(UpdateView):
    model = PetPhoto
    template_name = 'main/photo_edit.html'
    fields = ('description',)

    def get_success_url(self):
        return reverse_lazy('edit pet photo', kwargs= {'pk': self.object.id})

'''