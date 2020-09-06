from django.shortcuts import render

# Create your views here.

def StudentProfile(request):
    return render(request, 'e-learning/student_profile.html')