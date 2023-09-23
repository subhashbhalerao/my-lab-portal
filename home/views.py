from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def lab_rules(request):
    return render(request, 'home/lab-rules.html')

def tutorials(request):
    return render(request, 'home/tutorials.html')

def exp_lists(request):
    return render(request, 'home/experiment-lists.html')
