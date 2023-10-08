from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Exp_Lists

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def lab_rules(request):
    return render(request, 'home/lab-rules.html')

def tutorials(request):
    return render(request, 'home/tutorials.html')

def exp_lists(request):    
    db_data = Exp_Lists.objects.all().values()    
    return render(request, 'home/experiment-lists.html', {'db_data': db_data})

def exp_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        subject = request.POST['subject']
        exp_no = request.POST['exp-no']
        sem = request.POST['sem']
        dt = request.POST['dt']        
        myfile = request.FILES['myfile']
        faculty = request.POST['faculty']
        password = request.POST['password']

        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)        
        uploaded_file_url = fs.url(filename)        

        exp = Exp_Lists(subject=subject, exp_no=exp_no, sem=sem, dt=dt, file=uploaded_file_url, faculty=faculty)
        exp.save()
        
        return render(request, 'home/home.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'home/home.html')
      