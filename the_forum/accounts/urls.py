from django.contrib import admin
from django.urls import path, include

from the_forum.accounts.views import SignUpView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='register user'),
)

'''
urlpatterns = (
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)

'''