from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class lecturer(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=7)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    Organization = models.CharField(max_length=200)


    def __str__(self):
        return str(self.user)


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    starting_time = models.DateField(null=True)
    ending_time = models.DateField(null=True)
    lecture_id = models.ForeignKey(lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Notification(models.Model):
    noti_name = models.CharField(max_length=100, primary_key=True)
    user = models.ManyToManyField(User)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class HomeWork(models.Model):
    name = models.CharField(max_length=200)
    student_task = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.FloatField()
    def __str__(self):
        return self.name

class student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=7)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    Organization = models.CharField(max_length=200)
    Homework = models.ManyToManyField(HomeWork, through='DoHomeWork')
    #Registered_Courses = models.ManyToManyField(Cours')


    def __str__(self):
        return self.user.username

class Document(models.Model):
    doc_id = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    lecturer_id = models.CharField(max_length=15)
    course_id = models.CharField(max_length = 15)
    doc = models.FileField()
class DoHomeWork(models.Model):
    taken_date = models.DateTimeField(auto_now_add=True)
    homework = models.ForeignKey(HomeWork, on_delete=models.CASCADE)
    taken_student = models.ForeignKey(student, on_delete=models.CASCADE)
