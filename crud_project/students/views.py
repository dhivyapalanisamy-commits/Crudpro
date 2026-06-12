from django.shortcuts import render,redirect

# Create your views here.
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'students/form.html', {'form': form})

def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'students/form.html', {'form': form})

def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('list')

