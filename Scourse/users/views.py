from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
	return redirect('Moddle:index')

def register(request):
	"""Register a new user."""
	if request.method != 'POST':
		# Display blank registration form.
		form = UserCreationForm()
	else:
		# Process completed form
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			# Log the user in and then redirect to home page.
			login(request, new_user)
			return redirect('Moddle:index')

	# Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'registration/register.html', context)
def info(request):
	context = {}
	return render(request, 'registration/info.html', context)
def exit(request):
	logout(request)
	return redirect('Moddle:logout')
