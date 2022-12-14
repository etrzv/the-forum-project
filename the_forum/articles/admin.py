from django.contrib import admin
from django.utils.text import slugify
from the_forum.articles.models import Article
from the_forum.articles.forms import ArticleCreateForm, ArticleEditForm


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    add_form = ArticleCreateForm
    change_form = ArticleEditForm

    list_display = ('title', 'photo', 'content', )  # what appears on the search bar above the users
    list_filter = ('date_created', 'date_modified')    # filter on the right
    search_fields = ('title', )

    # prepopulated_fields = {'slug': ('slug', )}

    fieldsets = (
        (
            'Mandatory Information:',
            {
                'fields': (
                    'title',
                    'content',
                    'user',
                ),
            }
        ),
    )

    def get_form(self, request, obj=None, **kwargs):
        """
        Return a Form class for use in the admin add view. This is used by
        add_view and change_view.
        """
        if not obj:
            self.form = self.add_form
        else:
            self.form = self.change_form

        return super(ArticleAdmin, self).get_form(request, obj, **kwargs)

    # def get_fieldsets(self, request, obj=None):
    #     if not obj:
    #         fieldsets = self.add_fieldsets
    #         return fieldsets
    #     else:
    #         fieldsets = self.fieldsets
    #         return fieldsets

    # def save_model(self, request, obj, form, change):
    #     # don't overwrite manually set slug
    #     if form.cleaned_data['slug'] == "":
    #         # obj.slug = slugify(form.cleaned_data['id']) + "-" + slugify(form.cleaned_data['title'])
    #         obj.slug = slugify(f"{form.cleaned_data['id']}-{form.cleaned_data['title']}")
    #     obj.save()

