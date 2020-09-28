from django import forms
from .models import Letter
from django.utils.translation import gettext_lazy as _


class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ['title', 'img', 'comment', 'soldier_user', 'civil_user']
        labels = {
            'title': _('제목'),
            'img': _('사진'),
            'comment': _('코멘트'),
        }
        widgets = {
             'civil_user': forms.HiddenInput(),

        }
        help_texts = {
            'comment': _('일기를 작성해주세요.'),
        }


class UpdateLetterForm(LetterForm):
    class Meta:
        model = Letter
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LetterForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(LetterForm, self).save(commit=False)

        if commit:
            instance.save()
        return instance