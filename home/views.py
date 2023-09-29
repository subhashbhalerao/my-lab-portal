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

def exp_upload(request):
    subject = request.POST['subject']
    exp_no = request.POST['exp-no']
    sem = request.POST['sem']
    dt = request.POST['dt']
    file = request.POST['file']
    faculty = request.POST['faculty']
    password = request.POST['password']
    context = {'subject': subject, 'exp_no': exp_no, 'sem': sem, 'dt': dt, 'file': file,'faculty': faculty, 'password': password}
    return HttpResponse(f"Your entered info is - \n {context}")
    
      