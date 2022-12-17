from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('the_forum.common.urls')),
    path('accounts/', include('the_forum.accounts.urls')),
    path('articles/', include('the_forum.articles.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = "the_forum.common.exception_handlers.bad_request_custom_exception"
handler403 = "the_forum.common.exception_handlers.forbidden_custom_exception"
handler404 = "the_forum.common.exception_handlers.page_not_found_custom_exception"
handler500 = "the_forum.common.exception_handlers.server_error_custom_exception"
