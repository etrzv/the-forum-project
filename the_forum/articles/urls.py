from django.urls import path, include

from the_forum.articles.views import add_article

urlpatterns = (
    path('add/', add_article, name='add article'),
    # path('<str:username>/pet/<slug:pet_slug>/', include([
    #     path('', details_pet, name='details pet'),
    #     path('edit/', edit_pet, name='edit pet'),
    #     path('delete/', delete_pet, name='delete pet'),
    # ]))
)
