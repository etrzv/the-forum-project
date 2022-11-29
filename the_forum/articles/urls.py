from django.urls import path, include

from the_forum.articles.views import CreateArticleView, EditArticleView

urlpatterns = (
    path('add/', CreateArticleView.as_view(), name='add article'),
    path('<str:email>/article/<slug:article_slug>/', include([
        # path('', details_pet, name='details pet'),
        path('edit/', EditArticleView.as_view(), name='edit article'),
        # path('delete/', delete_pet, name='delete pet'),
    ]))
)
