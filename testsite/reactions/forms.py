from .models import TweetReaction, ImageReaction
from django import forms


class ImageReactionFormModel(forms.ModelForm):
    class Meta:
        ordering = ['-created_at']
        model = ImageReaction
        fields = ('image', 'user')
        widgets = {
            'image': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
        }


class TweetReactionFormModel(forms.ModelForm):
    class Meta:
        ordering = ['-created_at']
        model = TweetReaction
        fields = ('text', 'user')
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'comment',
                                           'rows': 10, 'cols': 10}),
        }