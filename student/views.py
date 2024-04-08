from django.shortcuts import render
from django.views import View
from .models import Student
from django.http import HttpResponse

class StudentListView(View):
    def get(self, request):
        search = request.GET.get('search')
        students = Student.objects.all()
        
        if not search:
            students = Student.objects.all()
            context = {
                "students": students,
                "search": search
            }
            return render(request, "student/student.html", context)
        else:
            students = students.filter(
                firts_name__icontains=search,  # Corrected typo here
                last_name__icontains=search,
                status__icontains=search
            )
            if students:
                context = {
                    "students": students,
                    "search": search
                }
                return render(request, "student/student.html", context)
            else:
                return render(request, "student/not_found.html")

class StudentDetailView(View):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        return render(request, "student/student_detail.html", {"student": student})

class LandingView(View):
    def get(self, request):
        return render(request, "index.html")
