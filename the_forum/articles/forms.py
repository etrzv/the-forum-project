from django import forms

from the_forum.articles.models import Article
from the_forum.common.models import ArticleLike, ArticleDislike, ArticleComment, ArticleBookmark


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'photo', 'content', )

        # labels = {
        #     "title": "Article's Title",
        #     "photo": 'Link to image (optional)',
        #     "content": "Article's Content",
        # }

        widgets = {
            'title': forms.Textarea(attrs={'rows': 1, 'cols': 20}),
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 20}),
        }


class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'photo', 'content', )

        widgets = {
            'title': forms.Textarea(attrs={'rows': 1, 'cols': 55}),
            'photo': forms.Textarea(attrs={'rows': 1, 'cols': 55}),
            'content': forms.Textarea(attrs={'rows': 15, 'cols': 73}),
        }


class ArticleDeleteForm(forms.ModelForm):
    def save(self, commit=True):
        likes = list(self.instance.articlelike_set.all())
        dislikes = list(self.instance.articledislike_set.all())
        comments = list(self.instance.articlecomment_set.all())
        bookmarks = list(self.instance.articlebookmarks_set.all())
        if commit:
            ArticleLike.objects.filter(articlelike__contains=likes).delete()
            ArticleDislike.objects.filter(articledislike__contains=dislikes).delete()
            ArticleComment.objects.filter(articlecomment__contains=comments).delete()
            ArticleBookmark.objects.filter(articlebookmark__contains=bookmarks).delete()
            self.instance.delete().delete()
        return self.instance

    class Meta:
        model = Article
        fields = ()
