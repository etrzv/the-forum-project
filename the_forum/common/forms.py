from django import forms

from the_forum.common.models import ArticleComment


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                    'placeholder': 'Add comment...'
                },
            ),
        }

# class PhotoCommentForm(forms.ModelForm):
#     class Meta:
#         model = PhotoComment
#         fields = ('text',)
#         widgets = {
#             'text': forms.Textarea(
#                 attrs={
#                     'cols': 40,
#                     'rows': 10,
#                     'placeholder': 'Add comment...'
#                 },
#             ),
#         }
#
#
# class SearchPhotosForm(forms.Form):
#     pet_name = forms.CharField(
#         max_length=50,
#         required=False,
#     )


