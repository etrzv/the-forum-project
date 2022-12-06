from django import forms

from the_forum.common.models import ArticleComment


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 138,
                    'rows': 10,
                    'placeholder': 'Add comment...'
                },
            ),
        }


class SearchArticleForm(forms.Form):
    title = forms.CharField(
        max_length=50,
        required=False,
    )

    widgets = {
        'title': forms.Textarea(
            attrs={
                'cols': 10,
                'rows': 1,
                'placeholder': 'Search...'
            },
        )
    }



