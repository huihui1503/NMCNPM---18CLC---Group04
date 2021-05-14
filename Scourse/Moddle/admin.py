from django.contrib import admin
from Moddle.models import Notification,lecturer, student, Course, User
# Register your models here.
class LecturerAdmin(admin.ModelAdmin):
	search_fields =['first_name','last_name','dob','gender','address','phone','email','Organization']

	list_filter = ['first_name','last_name','dob','gender','address','phone','email','Organization']

	list_display = ['first_name','last_name','dob','gender','address','phone','email','Organization']
	list_editable = ['dob','gender','phone','email']
admin.site.register(Course)
admin.site.register(lecturer,LecturerAdmin)
admin.site.register(student,LecturerAdmin)
admin.site.register(Notification)
