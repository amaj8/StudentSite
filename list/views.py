from django.shortcuts import render
from .models import Student
# Create your views here.
def RecordView(request):
    template_name='list/record.html'
    all_students = Student.objects.all().order_by('roll_num')
    context={'all_students':all_students}
    return render(request,template_name,context)

def HomeView(request):
    template_name = 'list/home.html'
    context={}
    return render(request,template_name,context)

def AboutView(request):
    template_name = 'list/about.html'
    context={}
    return render(request,template_name,context)

def ContactView(request):
    template_name = 'list/contact.html'
    context={}
    return render(request,template_name,context)

