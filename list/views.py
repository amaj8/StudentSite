from django.shortcuts import render
from .models import Student
# Create your views here.
def RecordView(request):
    template_name='list/record.html'
    all_students = Student.objects.all()
    context={'all_students':all_students}
    return render(request,template_name,context)

def HomeView(request):
    template_name = 'list/home.html'
    context={}
    return render(request,template_name,context)