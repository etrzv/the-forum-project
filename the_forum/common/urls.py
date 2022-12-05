from django.contrib import admin
from django.urls import path, include

from the_forum.common.views import HomeView, like_article, dislike_article, share_article, comment_article

urlpatterns = (
    path('', HomeView.as_view(), name='show index'),
    path('like/<int:article_id>/', like_article, name='like article'),
    path('dislike/<int:article_id>/', dislike_article, name='dislike article'),
    path('share/<int:article_id>/', share_article, name='share article'),
    path('comment/<int:article_id>/', comment_article, name='comment article'),
)

'''
from django.urls import path

from petstagram.common.views import index, like_photo, share_photo, comment_photo

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>/', like_photo, name='like photo'),
    path('share/<int:photo_id>/', share_photo, name='share photo'),
    path('comment/<int:photo_id>/', comment_photo, name='comment photo'),
)
'''

