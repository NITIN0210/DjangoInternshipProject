from django.shortcuts import render,redirect
from SchoolApp.forms import UsgForm,TeacherForm,StudentForm,StudentUsgForm,Chgepwd,StudentFullForm,TeacherFullForm,AttendanceForm,StudentAcademicsForm,StudentAcademicsTermForm
from SchoolApp.models import User,Teacher,Student,WorkingDates,Attendance,StudentAcademics,AttendanceCount,Mails
from School import settings
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
def home(req):
	return render(req,'app/home.html')
def about(req):
	return render(req,'app/about.html')
def contact(req):
	return render(req,'app/contact.html')

def userreg(req):
	if req.method=="POST":
		a=UsgForm(req.POST)
		c=TeacherForm(req.POST,req.FILES)
		if a.is_valid() and c.is_valid():
			b=a.save(commit=False)
			d=c.save(commit=False)
			b.email=d.email
			b.role=1
			d.tname=b.username
			d.tid=b.uid
			b.save()
			d.save()
			return redirect('/login')
	a=UsgForm()
	c=TeacherForm()
	return render(req,'app/userregister.html',{'a':a,'c':c})

def studentlist(req):
	f=Teacher.objects.get(tid=req.user.uid)
	y=Student.objects.filter(tsid=f.id)
	if req.method=="POST":
		a=StudentUsgForm(req.POST)
		b=StudentForm(req.POST,req.FILES)
		print(a,b)
		if a.is_valid() and b.is_valid():
			c=a.save(commit=False)
			d=b.save(commit=False)
			c.email=d.email
			c.role=2
			pswd=req.POST['pswd']
			d.sname=c.username
			d.sid=c.uid
			c.save()
			d.save()
			z1=StudentAcademics(said=d)
			z1.save()
			z2=Attendance(said=d)
			z2.save()
			z3=AttendanceCount(said=d)
			z3.save()
		sd = c.email
		sm = 'Password Authentication'
		mg = 'Hello '+c.username+' your password for school website is '+pswd+' .'
		rt = settings.EMAIL_HOST_USER
		dt = send_mail(sm,mg,rt,[sd])
		if dt == 1:
			messages.success(req,"Student added successfully and password reset mail is also sent!")
	a=StudentUsgForm()
	b=StudentForm()
	return render(req,'app/studentList.html',{'a':a,'b':b,'row1':f,'rows':y})
def changepwd(request):
	if request.method == "POST":
		k = Chgepwd(user=request.user,data=request.POST)
		if k.is_valid():
			k.save()
			return redirect('/login')
	k = Chgepwd(user=request)
	return render(request,'app/changepwd.html',{'t':k})
def stup(req,i):
	f=Teacher.objects.get(tid=req.user.uid)
	k=Student.objects.get(sid=i)
	if req.method=="POST":
		e=StudentFullForm(req.POST,req.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(req,"Student {} updated successfully".format(k.sname))
			return redirect('/slist')
	e=StudentFullForm(instance=k)
	return render(req,'app/stuupdate.html',{'x':e,'row1':f})

def stdl(req,i):
	k1=Student.objects.get(sid=i)
	k2=User.objects.get(uid=i)
	k3=StudentAcademics.objects.filter(said=i)
	k4=Attendance.objects.filter(said=i)
	k5=AttendanceCount.objects.filter(said=i)
	if req.method=="POST":
		k2.delete()
		k1.delete()
		k3.delete()
		k4.delete()
		k5.delete()
		messages.info(req,"Student {} deleted successfully".format(k1.sname))
		return redirect('/slist')
	return render(req,'app/studelete.html',{'r':k1})
def stview(req,i):
	k=Student.objects.get(sid=i)
	return render(req,'app/stview.html',{'R':k})

def pfle(req):
	a=User.objects.get(id=req.user.id)
	if a.role == 1:
		b=Teacher.objects.get(tid=a.uid)
	elif a.role == 2:
		b=Student.objects.get(sid=a.uid)
	if req.method=="POST":
		return render(req,'app/pupdate.html')
	return render(req,'app/profile.html',{'a':a,'b':b})

def profileupdate(req):
	a=User.objects.get(id=req.user.id)
	if a.role == 1 and req.method=="POST":
		x=Teacher.objects.get(tid=a.uid)
		b=TeacherFullForm(req.POST,req.FILES,instance=x)
		if b.is_valid():
			b.save()
			return redirect('/')
	elif a.role == 2 and req.method=="POST":
		x=Student.objects.get(sid=a.uid)
		b=StudentFullForm(req.POST,req.FILES,instance=x)
		if b.is_valid():
			b.save()
			return redirect('/')
	if a.role == 1:
		x=Teacher.objects.get(tid=a.uid)
		b=TeacherFullForm(instance=x)
	elif a.role == 2:
		x=Student.objects.get(sid=a.uid)
		b=StudentFullForm(instance=x)
	return render(req,'app/pupdate.html',{'row':b})
def attmark(req):
	x=Teacher.objects.get(tid=req.user.uid)
	a=Student.objects.filter(tsid=x.id)
	l=[]
	if req.method=="POST":
		d=req.POST['date']
		wd=WorkingDates.objects.all()
		datesForCheck=[]
		for i in wd:
			datesForCheck.append(i.dates.strftime('%Y-%m-%d'))
		#print(datesForCheck,type(d),d)
		if d in datesForCheck:
			#print('hello',d)
			return render(req,'app/atterror.html')
		wd=WorkingDates.objects.create(dates=d)
		wd.save()
		for j in a:
			l.append(j.sid)
		for i in l:
			p=req.POST.getlist(i)
			z=Student.objects.get(sid=i)
			z2=Attendance.objects.get(said=z,absentdates='2021-01-01')
			z3=AttendanceCount.objects.get(said=z)
			if p==[]:
				#print('absent\n')
				z3.attabsent+=1
				z2.absentdates=d
				z2.save()
				z3.save()

				z2=Attendance(said=z)
				z2.save()
			else:
				z3.attpresent+=1
				z3.save()
				#print('present\n')
	return render(req,'app/attendance.html',{'a':a})
#
def markmarks(req):
	c=StudentAcademics.objects.filter(term='DF')
	Term_Choices=[('DF','select Term'),('term1','Term1'),('term2','Term2'),('term3','Term3')]
	print(c)
	l=[]
	for j in c:
		l.append(j)
	for i in l:
		saidHere=str(i).strip('-')[0]+''+str(i).strip('-')[1]
		if req.method=="POST" and req.POST.get(saidHere):
			print(i,l,'1234',req.POST.get(saidHere))# and req.POST.get(i)
			# i=req.POST['said']
			# if req.POST.get('i'):
			
			# print(saidHere)
			t=req.POST['term']
			k=Student.objects.get(sid=saidHere)
			a=StudentAcademicsForm(req.POST,instance=k)
			print(a)
			if a.is_valid():
				#print(saidHere)
				for i in Term_Choices:
					if i[0]==t:
						te=Term_Choices.index(i)
				a.term=Term_Choices[te][1]
				a.save()
				# z=StudentAcademics(said=k)
				# z.save()
				print('hello')
	inst=[]
	for j in c:
		inst.append(StudentAcademicsForm(instance=j))
	#a=StudentAcademicsForm()
	b=StudentAcademicsTermForm()
	return render(req,'app/marks.html',{'a':inst,'b':b,'c':c})
#hidden and then assign and see


def markmarks2(req):
	c=StudentAcademics.objects.filter(term='DF')
	b=StudentAcademicsTermForm()
	l=[]
	for j in c:
		l.append(j)
	ss=[]
	f=['english','telugu','maths','science','social']
	for i in l:
		for j in f:
			ss.append(j+''+str(i))
	if req.method=='POST':
		b=StudentAcademicsTermForm(req.POST)
		if b.is_valid():
			t=b.cleaned_data['term']
		termCheck=StudentAcademics.objects.all()
		termCheckList=[]
		for i in termCheck:
			termCheckList.append(i.term)
			#print(datesForCheck,type(d),d)
		if t in termCheckList:
			#print('hello',t)
			return render(req,'app/atterror.html')
		vl=[]
		for i in ss:
			vl.append(req.POST[i])
		for i in range(len(vl)//5):
			j=(len(vl)//5)*i
			x=Student.objects.get(sid=str(l[i]).strip('-')[0]+''+str(l[i]).strip('-')[1])
			#print(len(vl),i,j+0,j+1,j+2,j+3,j+4)
			a=StudentAcademics(said=x,term=t,english=vl[j+0],telugu=vl[j+1],maths=vl[j+2],science=vl[j+3],social=vl[j+4])
			a.save()
	return render(req,'app/marks2.html',{'l':l,'b':b,'f':f})

def smd(req):
	id=req.user.uid
	a=Student.objects.get(sid=id)
	b=StudentAcademics.objects.filter(said=a)

	return render(req,'app/studentmarksdisplay.html',{'a':a,'b':b})
def sad(req):
	id=req.user.uid
	a=Student.objects.get(sid=id)
	d=AttendanceCount.objects.get(said=a)
	b=Attendance.objects.filter(said=a)
	c=WorkingDates.objects.all()
	l=[]
	for i in b:
		l.append(i.absentdates)
	print(d)
	per=int((d.attpresent/(d.attpresent+d.attabsent))*100)
	print(per)
	return render(req,'app/studentattendancedisplay.html',{'a':a,'c':c,'l':l,'d':d,'per':per})
def smailtot(req):
	id=req.user.uid
	a=Student.objects.get(sid=id)
	b=Teacher.objects.get(id=a.tsid_id)

	if req.method=="POST":
		sd = req.POST['snmail'].split(',')
		sm = req.POST['sub']
		mg = req.POST['msg']
		rt = settings.EMAIL_HOST_USER
		c=Mails(smail=a.email,rmail=b.email,sub=sm,body=mg,sid=id,tid=b.tid,senderid=a.sid)
		c.save()
		dt = send_mail(sm,mg,rt,sd)
		if dt == 1:
			return redirect('/stmailtach')

	return render(req,'app/studentmailtoteacher.html',{'a':a,'b':b})
def svmsg(req):
	id=req.user.uid
	a=Student.objects.get(sid=id)
	b=Teacher.objects.get(id=a.tsid_id)
	d=b.email
	c=Mails.objects.filter(sid=a.sid,tid=b.tid)
	return render(req,'app/viewmessage.html',{'a':a,'b':b,'c':c,'d':d})
def tvmsg(req,i):
	a=Student.objects.get(sid=i)	
	print(i)
	id=req.user.uid
	b=Teacher.objects.get(tid=id)	
	d=a.email

	sa=StudentAcademics.objects.filter(said=a)
	att=Attendance.objects.filter(said=a)
	attC=AttendanceCount.objects.get(said=a)
	attPresentPer=int((attC.attpresent/(attC.attpresent+attC.attabsent))*100)

	wd=WorkingDates.objects.all()
	l=[]
	for j in att:
		l.append(j.absentdates)

	if req.method=="POST":
		sd = req.POST['snmail'].split(',')
		sm = req.POST['sub']
		mg = req.POST['msg']
		rt = settings.EMAIL_HOST_USER
		c=Mails(smail=b.email,rmail=a.email,sub=sm,body=mg,sid=i,tid=b.tid,senderid=b.tid)
		c.save()
		dt = send_mail(sm,mg,rt,sd)
		if dt == 1:
			return redirect('/tecviewmesg/{}/'.format(i))

	c=Mails.objects.filter(sid=a.sid,tid=b.tid)
	return render(req,'app/teacherviewmessage.html',{'a':a,'b':b,'c':c,'d':d,'wd':wd,'l':l,'sa':sa,'per':attPresentPer,'attC':attC})
