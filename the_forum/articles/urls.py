from django.urls import path, include

from the_forum.articles.views import ArticleCreateView, ArticleDetailsView, ArticleEditView, ArticleDeleteView

urlpatterns = (
    path('add/', ArticleCreateView.as_view(), name='add article'),
    path('article/<slug:slug>/', include([
        path('', ArticleDetailsView.as_view(), name='details article'),
        path('edit/', ArticleEditView.as_view(), name='edit article'),
        path('delete/', ArticleDeleteView.as_view(), name='delete article'),
    ]))
)

# str - Matches any non-empty string, excluding the path separator, '/'.
# This is the default if a converter isn’t included in the expression.

# slug - Matches any slug string consisting of ASCII letters or numbers,
# plus the hyphen and underscore characters. For example, building-your-1st-django-site.
