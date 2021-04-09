from django.contrib import admin
from Moddle.models import Notification,lecturer, student, Course
# Register your models here.

admin.site.register(Course)
admin.site.register(lecturer)
admin.site.register(student)
admin.site.register(Notification)
