from django import forms
from .models import Bug, Comment

class AddBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('name', 'description', 'bug_or_feature')
        
class EditBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('name', 'description', 'bug_or_feature')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )