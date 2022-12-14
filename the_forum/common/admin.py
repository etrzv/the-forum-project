from django.contrib import admin

from the_forum.common.forms import ArticleCommentForm
from the_forum.common.models import ArticleComment, ArticleLike, ArticleDislike, ArticleBookmark, CommentLike, \
    CommentDislike


@admin.register(ArticleComment)
class CommentAdmin(admin.ModelAdmin):
    add_form = ArticleCommentForm

    list_display = ('text', 'article', 'user', )  # what appears on the search bar above the users
    list_filter = ('publication_date', 'article', 'user', )    # filter on the right
    search_fields = ('text', )

    # prepopulated_fields = {'slug': ('slug', )}

    fieldsets = (
        (
            'Mandatory Information:',
            {
                'fields': (
                    'text',
                    'article',
                    'user',
                ),
            }
        ),
    )

    # def get_form(self, request, obj=None, **kwargs):
    #     """
    #     Return a Form class for use in the admin add view. This is used by
    #     add_view and change_view.
    #     """
    #     if not obj:
    #         self.form = self.add_form
    #     else:
    #         self.form = self.change_form
    #
    #     return super(ArticleAdmin, self).get_form(request, obj, **kwargs)

    # list_display = ('name', 'body', 'post', 'created_on', 'active')
    # list_filter = ('active', 'created_on')
    # search_fields = ('name', 'email', 'body')

    # actions = ['approve_comments']

    # def approve_comments(self, request, queryset):
    #     queryset.update(active=True)


@admin.register(ArticleLike)
class ArticleLikeAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', )
    search_fields = ('article', 'user',)

    fieldsets = (
        (
            'Mandatory Information:',
            {
                'fields': (
                    'article',
                    'user',
                ),
            }
        ),
    )


@admin.register(ArticleDislike)
class ArticleDislikeAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', )
    search_fields = ('article', 'user',)

    fieldsets = (
        (
            'Mandatory Information:',
            {
                'fields': (
                    'article',
                    'user',
                ),
            }
        ),
    )


@admin.register(ArticleBookmark)
class ArticleBookmarkAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', )
    search_fields = ('article', 'user',)

    fieldsets = (
        (
            'Mandatory Information:',
            {
                'fields': (
                    'article',
                    'user',
                ),
            }
        ),
    )


@admin.register(CommentLike)
class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', )
    search_fields = ('comment', 'user', )

    fieldsets = (
        (
            'Mandatory Information:',
            {
                'fields': (
                    'comment',
                    'user',
                ),
            }
        ),
    )


@admin.register(CommentDislike)
class CommentDislikeAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', )
    search_fields = ('comment', 'user',)

    fieldsets = (
        (
            'Mandatory Information:',
            {
                'fields': (
                    'comment',
                    'user',
                ),
            }
        ),
    )
