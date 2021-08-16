from SchoolApp.models import User,Teacher,Student,Attendance,StudentAcademics
from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

class UsgForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"enter password",
		}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"confirm password"
		}))
	class Meta:
		model=User
		fields=['username',"uid"]
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter name",
			}),
		"uid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter your uniqueId",
			}),
		}
class StudentUsgForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"enter password"
		}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"confirm password"
		}))
	class Meta:
		model=User
		fields=['username',"uid"]
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter Student's name",
			}),
		"uid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter Student's uniqueId",
			}),
		}
class TeacherForm(forms.ModelForm):
	class Meta:
		model=Teacher
		fields=['email','mobile','gender','timage','standard']
		Gender_Choices=[('M','Male'),('F','FeMale')]
		widgets={
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter email",
			}),
		"mobile":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter your MobileNo",
			}),
		"gender":forms.RadioSelect(choices=Gender_Choices),
		"standard":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"select Standard",
			}),
		}
class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields=['tsid','email','mobile','gender','simage']
		Gender_Choices=[('M','Male'),('F','FeMale')]
		widgets={
		"tsid":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter email",
			}),
		"mobile":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter student's MobileNo",
			}),
		"gender":forms.RadioSelect(choices=Gender_Choices),
		
		}
class Chgepwd(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Old Password"
		}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter New Password",
		}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter New Confirm Password",
		}))
	class Meta:
		model = User
		fields = ["old_password","new_password1","new_password2"]
class StudentFullForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'
		Gender_Choices=[('M','Male'),('F','FeMale')]
		widgets={
		'sname':forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter sname",
			}),
		'email':forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter email",
			}),		
		'sid':forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter sid",
			}),
		'mobile':forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter mobileNo",
			}),
		"gender":forms.RadioSelect(choices=Gender_Choices),
		"tsid":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}
class TeacherFullForm(forms.ModelForm):
	class Meta:
		model=Teacher
		fields=['tname','tid','email','mobile','gender','timage','standard']
		Gender_Choices=[('M','Male'),('F','FeMale')]
		widgets={
		"tname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter name",
			}),
		"tid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter tid",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter email",
			}),
		"mobile":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter your MobileNo",
			}),
		"gender":forms.RadioSelect(choices=Gender_Choices),
		"standard":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"select Standard",
			}),
		}

class AttendanceForm(forms.Form):
	class Meta:
		model=Attendance
		fields=['said']
		
		
class StudentAcademicsForm(forms.ModelForm):
	class Meta:
		model=StudentAcademics
		fields=['said','english','telugu','maths','science','social']
		widgets={
		"said":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter said",
			}),
		"english":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter english marks",
			}),
		"telugu":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter telugu marks",
			}),
		"maths":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter maths marks",
			}),
		"science":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter science marks",
			}),
		"social":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter social marks",
			}),
		}
class StudentAcademicsTermForm(forms.ModelForm):
	class Meta:
		model=StudentAcademics
		fields=['term']
		widgets={
		"term":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"select term",
			'Required':True,
			}),
		}
		
		

		
