from django.contrib import admin
from .models import Tutor, Student

# Register your models here.

class TutorAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Tutor)


class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Student)