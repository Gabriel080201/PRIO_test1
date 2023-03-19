from django.http import HttpResponse as respond
from django.shortcuts import render

def webPage_1(request):
    return render(request, 'ViewSchedule.html')

def webPage_2(request):
    return render(request, 'add_task.html')

def webPage_3(request):
    return render(request, 'add_subject.html')