from django.contrib import admin
from Moddle.models import Notification,lecturer, student, Course, User,Document
# Register your models here.
class LecturerAdmin(admin.ModelAdmin):
	search_fields =['first_name','last_name','dob','gender','address','phone','email','Organization']

	list_filter = ['first_name','last_name','dob','gender','address','phone','email','Organization']

	list_display = ['first_name','last_name','dob','gender','address','phone','email','Organization']
	list_editable = ['dob','gender','phone','email']
class DocumentAdmin(admin.ModelAdmin):
	search_fields =['doc_id','name','lecturer_id','course_id','address','doc']
	list_filter = ['doc_id','name','lecturer_id','course_id','address','doc']

	list_display =['doc_id','name','lecturer_id','course_id','address','doc']
	list_editable = ['doc_id','name','lecturer_id','course_id','address','doc']
    
admin.site.register(Course)
admin.site.register(lecturer,LecturerAdmin)
admin.site.register(student,LecturerAdmin)
admin.site.register(Notification)
admin.site.register(Document)
