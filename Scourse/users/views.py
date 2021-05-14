from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from Moddle.models import User,student,lecturer

# Create your views here.
def index(request):
	return redirect('Moddle:index')

def register_view(request):
	return render(request, 'register_view.html')

class StudentRegister(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User

	def save(self):
		new_user = super().save(commit=False)
		new_user.is_student = True
		new_user.save()
		new_student = student.objects.create(user=new_user)
		return new_user

class TeacherRegister(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User

	def save(self):
		new_user = super().save(commit=False)
		new_user.is_teacher = True
		new_user.save()
		new_student = lecturer.objects.create(user=new_user)
		return new_user

def register_student_form(request):
	"""Register a new user."""
	if request.method != 'POST':
		form = StudentRegister()
	else:
		form = StudentRegister(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			# Log the user in and then redirect to home page.
			login(request, new_user)
			return redirect('Moddle:student')

	# Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'registration/register_student.html', context)

def register_teacher_form(request):
	"""Register a new user."""
	if request.method != 'POST':
		form = TeacherRegister()
	else:
		form = TeacherRegister(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			# Log the user in and then redirect to home page.
			login(request, new_user)
			return redirect('Moddle:teacher')

	# Display a blank or invalid form.
	context = {'form': form}
<<<<<<< HEAD
	return render(request, 'registration/register_teacher.html', context)

=======
	return render(request, 'registration/register.html', context)
def info(request):
	context = {}
	return render(request, 'registration/info.html', context)
>>>>>>> 27018f97818af9ebc4d08d02bdba746b0fdc5bc6
def exit(request):
	logout(request)
	return redirect('Moddle:logout')
