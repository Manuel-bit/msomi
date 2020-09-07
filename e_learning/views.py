from django.shortcuts import render
from .decorators import allowed_users, TutorRedirect
from django.contrib.auth.decorators import login_required
from users.forms import UserUpdateForm,StudentUpdateForm

# Create your views here.
@login_required(login_url='login')
@TutorRedirect
def StudentProfile(request):
    return render(request, 'e-learning/student_profile.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['colleges'])
def TutorProfile(request):
    return render(request, 'e-learning/tutor_profile.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        sp_form = StudentUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.student)
        if u_form.is_valid() and sp_form.is_valid():
            u_form.save()
            sp_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        sp_form = StudentUpdateForm(instance=request.user.student)

    context = {
        'u_form': u_form,
        'sp_form': sp_form
    }

    return render(request, 'e-learning/student_update.html', context)