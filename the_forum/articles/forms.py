from django import forms

from the_forum.articles.models import Article


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
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 20})
        }


class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'photo', 'content', )

        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 20})
        }


'''
from django import forms

from petstagram.core.form_mixins import DisabledFormMixin
from petstagram.pets.models import Pet


# `ModelForm` and `Form`:
# - `ModelForm` binds to models
# - `Form` is detached from models

class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        # fields = '__all__' (not the case, we want to skip `slug`
        fields = ('name', 'date_of_birth', 'personal_photo')
        # exclude = ('slug',)
        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name'
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            )
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(DisabledFormMixin, PetBaseForm):
    disabled_fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


class PetDeleteForm(DisabledFormMixin, PetBaseForm):
    disabled_fields = ('name', 'date_of_birth', 'personal_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


'''