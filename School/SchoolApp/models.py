from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
	t=[(1,'Teacher'),(2,'Student')]
	role=models.IntegerField(choices=t)
	uid=models.CharField(max_length=10)
	email=models.EmailField(max_length=30)
class Teacher(models.Model):
	Gender_Choices=[('M','Male'),('F','FeMale')]
	Standar_Choices=[('DF','selectClass'),('class1','Class1'),('class2','Class2'),('class3','Class3')]
	tname=models.CharField(max_length=20)
	tid=models.CharField(max_length=10)#,primary_key=True
	email=models.EmailField(max_length=30)
	mobile=models.IntegerField()
	gender=models.CharField(choices=Gender_Choices,default='M',max_length=10)
	timage=models.ImageField(upload_to='TeacherImages/',default='logo.png')
	standard=models.CharField(choices=Standar_Choices,max_length=10,default='DF')

	def __str__(self):
		return self.tname+"-"+self.tid+"-"+self.standard

class Student(models.Model):
	Gender_Choices=[('M','Male'),('F','FeMale')]
	sname=models.CharField(max_length=20)
	sid=models.CharField(max_length=10,primary_key=True)
	email=models.EmailField(max_length=30)
	mobile=models.IntegerField()
	gender=models.CharField(choices=Gender_Choices,default='M',max_length=10)
	simage=models.ImageField(upload_to='StudentImages/',default='logo.png')
	tsid=models.ForeignKey(Teacher,on_delete=models.CASCADE)
	def __str__(self):
		return self.sid+'-'+self.sname
class StudentAcademics(models.Model):
	Term_Choices=[('DF','select Term'),('term1','Term1'),('term2','Term2'),('term3','Term3')]
	said=models.ForeignKey(Student,on_delete=models.CASCADE)
	term=models.CharField(choices=Term_Choices,max_length=10,default='DF')
	english=models.IntegerField(default=0)
	telugu=models.IntegerField(default=0)
	maths=models.IntegerField(default=0)
	science=models.IntegerField(default=0)
	social=models.IntegerField(default=0)
	def __str__(self):
		return str(self.said)
	
class AttendanceCount(models.Model):
	said=models.ForeignKey(Student,on_delete=models.CASCADE)
	attpresent=models.IntegerField(default=0)
	attabsent=models.IntegerField(default=0)

class Attendance(models.Model):
	said=models.ForeignKey(Student,on_delete=models.CASCADE)
	absentdates=models.DateField(default='2021-01-01')
class WorkingDates(models.Model):
	dates=models.DateField()

class Mails(models.Model):
	smail = models.EmailField(max_length=30)
	rmail = models.EmailField(max_length=30)
	sub = models.CharField(max_length=50)
	body = models.CharField(max_length=200)
	date = models.DateTimeField(default=timezone.now)
	sid = models.CharField(max_length=10)
	tid = models.CharField(max_length=10)
	senderid = models.CharField(max_length=10,default='a')
	