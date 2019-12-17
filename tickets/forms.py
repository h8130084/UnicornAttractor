from django import forms
from .models import Bug, Comment

class AddBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('name', 'description', 'bug_or_feature')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'text-input', 'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'class': 'text-box', 'placeholder': 'Enter your description'}),
            'bug_or_feature': forms.Select(attrs={'class': 'select-input'})
        }
        
class EditBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('name', 'description', 'bug_or_feature')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'text-input', 'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'class': 'text-box', 'placeholder': 'Enter your description'}),
            'bug_or_feature': forms.Select(attrs={'class': 'select-input'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )
        labels = {'body': 'Comment'}
        widgets = {
            'body': forms.Textarea(attrs={'class': 'text-box', 'placeholder': 'Enter your comment'}),
        }
        