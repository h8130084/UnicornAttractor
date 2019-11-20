from django.shortcuts import render, redirect, reverse

# Create your views for tickets here.

def bug(request):
    return render(request, 'bug.html')
    

def addBug(request):
    return render(request, 'add_bug.html')