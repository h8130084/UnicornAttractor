from django.shortcuts import render, redirect, reverse
from .models import Bug
from .forms import AddBugForm

# Create your views for tickets here.

def bug(request):
    
    return render(request, 'bug.html')
    

def addBug(request):
    
    if request.method == 'POST':
        add_bug_form = AddBugForm(request.POST)
    
        if add_bug_form.is_valid():
            new_bug = add_bug_form.save()
            return redirect(reverse('bug'))
    else:
        add_bug_form = AddBugForm
    
    return render(request, 'add_bug.html', {'add_bug_form': add_bug_form})
    
    
def all_bugs(request):
    bugs = Bug.objects.all()
    return render (request, "bug.html", {"bugs": bugs})