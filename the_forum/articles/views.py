from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from core.utils import apply_likes_count, apply_dislikes_count, apply_likes_count_for_comment, \
    apply_dislikes_count_for_comment
from the_forum.accounts.models import Profile
from the_forum.articles.forms import ArticleCreateForm, ArticleEditForm, ArticleDeleteForm
from the_forum.articles.models import Article
from the_forum.common.forms import ArticleCommentForm, SearchArticleForm
from the_forum.common.models import ArticleComment, ArticleLike, ArticleDislike, ArticleBookmark, CommentLike

# Create your views here.

# The GET method, which was used in the example earlier, appends name/value pairs to the URL. Unfortunately,
# the length of a URL is limited, so this method only works if there are only a few parameters.
# The URL could be truncated if the form uses a large number of parameters, or if the parameters contain large amounts
# of data. Also, parameters passed on the URL are visible in the address field of the browser not the best place for
# a password to be displayed.

# The alternative to the GET method is the POST method. This method packages the name/value pairs inside the body
# of the HTTP request, which makes for a cleaner URL and imposes no size limitations on the forms output.
# It is also more secure.


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
    search_form = SearchArticleForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.model.objects.get(slug=self.object.slug)
        context.update({
            'form_class': self.form_class(instance=article),
            'search_form': self.search_form,
        })
        return context

    def get_success_url(self):
        return reverse_lazy('edit article', kwargs={'slug': self.object.slug})


class ArticleDetailsView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'articles/article-details-page.html'
    form_class = ArticleCommentForm
    search_form = SearchArticleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        article = Article.objects.get(id=self.object.pk)
        likes = [apply_likes_count(article)]
        dislikes = [apply_dislikes_count(article)]

        user = UserModel.objects.get(id=self.request.user.pk)
        profile = Profile.objects.get(user_id=user.id)

        user_likes_articles = ArticleLike.objects.filter(article_id=article.id, user_id=user.pk)
        user_dislikes_articles = ArticleDislike.objects.filter(article_id=article.id, user_id=user.pk)
        # user_bookmarks_articles = ArticleBookmark.objects.filter(article_id=article.id, user_id=user.pk)

        # article, articlebookmark, articlecomment, articledislike, articlelike, date_joined, email,
        # groups, id, is_active, is_staff, is_superuser, last_login, logentry, password, profile, user_permissions

        # comments = ArticleComment.objects.filter(article_id=article.id) # both work
        comments = article.articlecomment_set.all()
        quantity_comments = len(comments)
        comment_likes = [apply_likes_count_for_comment(comment) for comment in comments]
        comment_dislikes = [apply_dislikes_count_for_comment(comment) for comment in comments]

        # user_likes_comments = CommentLike.objects.filter(comment(comment_id=comment.id, user_id=user.pk)
        #                                                  for comment in comments)

        context.update({
            'search_form': self.search_form,

            'article': article,
            'likes': likes,
            'dislikes': dislikes,

            'user': user,
            'profile': profile,
            'is_owner': article.user == self.request.user,
            'has_user_liked_article': user_likes_articles,
            'has_user_disliked_article': user_dislikes_articles,

            'comments': comments,
            'quantity_comments': quantity_comments,
            'comment_form': self.form_class,
            'comment_likes': comment_likes,
            'comment_dislikes': comment_dislikes,
            'is_comment_owner': article.user == self.request.user,

            # 'user_likes_comments': user_likes_comments,

        })

        return context


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'articles/article-delete-page.html'
    model = Article
    success_url = reverse_lazy('show index')
    form_class = ArticleDeleteForm
    search_form = SearchArticleForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.search_form
        return context


