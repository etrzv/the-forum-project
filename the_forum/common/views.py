import pyperclip as pyperclip
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from core.utils import apply_likes_count, apply_dislikes_count
from the_forum.accounts.forms import UserCreateForm
from the_forum.articles.models import Article
from the_forum.articles.utils import get_article_url
from the_forum.common.forms import ArticleCommentForm, SearchArticleForm
from the_forum.common.models import ArticleLike, ArticleDislike, ArticleBookmark, ArticleComment, CommentLike, \
    CommentDislike

UserModel = get_user_model()


def index(request):
    search_form = SearchArticleForm(request.GET)
    search_pattern = None

    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['title']

    articles = Article.objects.all().order_by('-date_created')

    if search_pattern:
        articles = articles.filter(title__contains=search_pattern).order_by('-date_created')

    likes = [apply_likes_count(article) for article in articles]
    dislikes = [apply_dislikes_count(article) for article in articles]

    context = {
        'articles': articles,
        'search_form': search_form,
        'likes': likes,
        'dislikes': dislikes,

    }

    return render(
        request,
        'common/home-page.html',
        context,
    )


@login_required
def like_article(request, article_id):
    # articles have - id, slug, user_id fields
    #                                         accepts field names as kwargs
    user_liked_articles = ArticleLike.objects.filter(article_id=article_id, user_id=request.user.pk)
    user_disliked_articles = ArticleDislike.objects.filter(article_id=article_id, user_id=request.user.pk)

    if user_liked_articles:
        user_liked_articles.delete()
    elif user_disliked_articles:
        user_disliked_articles.delete()
        ArticleLike.objects.create(article_id=article_id, user_id=request.user.pk)
    else:
        ArticleLike.objects.create(article_id=article_id, user_id=request.user.pk)

    # A dictionary containing all available HTTP headers. Available headers depend on the client and server
    return redirect(get_article_url(request, article_id))


@login_required
def dislike_article(request, article_id):
    # articles have - id, slug, user_id fields
    #                                         accepts field names as kwargs
    user_disliked_articles = ArticleDislike.objects.filter(article_id=article_id, user_id=request.user.pk)
    user_liked_articles = ArticleLike.objects.filter(article_id=article_id, user_id=request.user.pk)

    if user_disliked_articles:
        user_disliked_articles.delete()
    elif user_liked_articles:
        user_liked_articles.delete()
        ArticleDislike.objects.create(article_id=article_id, user_id=request.user.pk)
    else:
        ArticleDislike.objects.create(article_id=article_id, user_id=request.user.pk)
    # A dictionary containing all available HTTP headers. Available headers depend on the client and server
    return redirect(get_article_url(request, article_id))


@login_required
def bookmark_article(request, article_id):
    user_bookmarked_articles = ArticleBookmark.objects.filter(article_id=article_id, user_id=request.user.pk)

    if user_bookmarked_articles:
        # user_bookmarked_article = ArticleBookmark.objects.get(article_id=article_id, user_id=request.user.pk)
        user_bookmarked_articles.delete()
        # user_bookmarked_article.delete()
    else:
        ArticleBookmark.objects.create(article_id=article_id, user_id=request.user.pk)
    return redirect(get_article_url(request, article_id))


@login_required
def comment_article(request, article_id, user_id):
    article = Article.objects.get(pk=article_id)
    user = UserModel.objects.get(pk=user_id)

    if request.method == 'POST':
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # Does not persist to DB
            comment.article = article
            comment.user = user
            comment.save()

    return redirect(get_article_url(request, article_id))


@login_required
def comment_like(request, article_id, comment_id):
    user_liked_comments = CommentLike.objects.filter(comment_id=comment_id, user_id=request.user.pk)
    user_disliked_comments = CommentDislike.objects.filter(comment_id=comment_id, user_id=request.user.pk)

    if user_liked_comments:
        user_liked_comments.delete()
    elif user_disliked_comments:
        user_disliked_comments.delete()
        CommentLike.objects.create(comment_id=comment_id, user_id=request.user.pk)
    else:
        CommentLike.objects.create(comment_id=comment_id, user_id=request.user.pk)

    return redirect(get_article_url(request, article_id))


@login_required
def comment_dislike(request, article_id, comment_id):
    user_disliked_comments = CommentDislike.objects.filter(comment_id=comment_id, user_id=request.user.pk)
    user_liked_comments = CommentLike.objects.filter(comment_id=comment_id, user_id=request.user.pk)

    if user_disliked_comments:
        user_disliked_comments.delete()
    elif user_liked_comments:
        user_liked_comments.delete()
        CommentDislike.objects.create(comment_id=comment_id, user_id=request.user.pk)
    else:
        CommentDislike.objects.create(comment_id=comment_id, user_id=request.user.pk)

    return redirect(get_article_url(request, article_id))
