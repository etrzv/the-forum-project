from django.contrib import admin
from django.urls import path, include

from the_forum.common.views import index, like_article, dislike_article, comment_article, \
    bookmark_article, comment_like, comment_dislike

urlpatterns = (
    path('', index, name='show index'),
    path('like/<int:article_id>/', like_article, name='like article'),
    path('dislike/<int:article_id>/', dislike_article, name='dislike article'),
    path('bookmark/<int:article_id>/', bookmark_article, name='bookmark article'),
    path('comment/<int:article_id>/<int:user_id>', comment_article, name='comment article'),
    path('like/<int:article_id>/<int:comment_id>', comment_like, name='like comment'),
    path('dislike/<int:article_id>/<int:comment_id>', comment_dislike, name='dislike comment'),
)
