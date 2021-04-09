from django.db import models

# Create your models here.
class student(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=7)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    Organization = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id

    def is_type(x):
        return x == 'student'

class lecturer(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=7)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    Organization = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id

    def is_type(x):
        return x == 'lecturer'

class Notification(models.Model):
    nof_id = models.CharField(max_length=10, primary_key=True)
    user = models.CharField(max_length=10)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    starting_time = models.DateField()
    ending_time = models.DateField()
    lecture_id = models.ForeignKey(lecturer, on_delete=models.CASCADE)
    def __str__(self):
        return self.text
