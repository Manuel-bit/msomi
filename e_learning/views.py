from django.shortcuts import render
from .decorators import allowed_users, TutorRedirect
from django.contrib.auth.decorators import login_required
from users.models import Tutor,Student,Course

# Create your views here.
@login_required(login_url='login')
@TutorRedirect
def StudentProfile(request):
    return render(request, 'e-learning/student_profile.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['colleges'])
def TutorProfile(request):
    return render(request, 'e-learning/tutor_profile.html')

def Courses(request):
    current_user = request.user
    courses = Course.objects.filter(students__user__id=current_user.id)
    return render(request, 'e-learning/courses.html', {'courses':courses})

