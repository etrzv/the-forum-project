from django import forms

from the_forum.common.models import ArticleComment


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 109,
                    'rows': 8,
                    'placeholder': 'Add a comment...'
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = ''


class SearchArticleForm(forms.Form):
    title = forms.CharField(
        max_length=50,
        required=False,
        label='',
    )

    widgets = {
        'title': forms.Textarea(
            attrs={
                'cols': 10,
                'rows': 1,
                'placeholder': 'Search...',
            },
        )
    }
