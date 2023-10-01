from django import forms
from .models import Draft


class DraftForm(forms.ModelForm):
    class Meta:
        model = Draft
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs = {'class': 'text-center title-input', 'placeholder': 'Title'}),
            'content': forms.Textarea(
                attrs = {'class': 'writing-area', 'rows': 18, 'placeholder': 'Start writing here...'}),
        }
