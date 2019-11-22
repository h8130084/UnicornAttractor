from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Bug
from .forms import AddBugForm, CommentForm

# Create your views for tickets here.


    

def addBug(request):
    
    if request.method == 'POST':
        add_bug_form = AddBugForm(request.POST)
    
        if add_bug_form.is_valid():
            new_bug = add_bug_form.save()
            return redirect(reverse('bug'))
    else:
        add_bug_form = AddBugForm
    
    return render(request, 'add_bug.html', {'add_bug_form': add_bug_form})
    
    
def bug(request):
    bugs = Bug.objects.all()
    return render(request, "bug.html", {"bugs": bugs})
    

def bugDetails(request, pk):
    
    bug = get_object_or_404(Bug, pk=pk)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.bugID = bug.id
            
    
    return render(request, 'bug_details.html', {'bug': bug, 'comment_form': comment_form})