from django.contrib import admin
from .models import student_profile,teacher_profile,question,answer
# Register your models here.
admin.site.register(student_profile),
admin.site.register(teacher_profile),
admin.site.register(question),
admin.site.register(answer),