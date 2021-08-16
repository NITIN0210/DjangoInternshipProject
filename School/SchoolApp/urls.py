from django.urls import path
from SchoolApp import views
from django.contrib.auth import views as v

urlpatterns=[
	path('',views.home,name='hm'),
	path('abt/',views.about,name="ab"),
	path('cntc/',views.contact,name='ct'),

	path('rg/',views.userreg,name='reg'),
	path('login/',v.LoginView.as_view(template_name="app/loginView.html"),name="lg"),
	path('logout/',v.LogoutView.as_view(template_name="app/logoutView.html"),name="lgo"),
	path('chge/',views.changepwd,name="chpd"),
	
	path('slist/',views.studentlist,name="slist"),
	path('stup/<str:i>/',views.stup,name="stup"),
	path('stdl/<str:i>/',views.stdl,name="stdl"),
	path('stview/<str:i>/',views.stview,name="rsv"),

	path('pfle/',views.pfle,name='pf'),
	path('pup/',views.profileupdate,name='pu'),

	path('attendance/',views.attmark,name="att"),
	#path('mt/',views.markterm,name="mt"),
	path('marks/',views.markmarks2,name="mm"),

	path('smarksdisplay/',views.smd,name='smd'),
	path('sattendancedisplay/',views.sad,name='sad'),
	path('stmailtach/',views.smailtot,name='smailtot'),

	path('stdviewmesg/',views.svmsg,name='svmsg'),
	path('tecviewmesg/<str:i>/',views.tvmsg,name='tvmsg'),

]

# It's possible to use django built-in widthratio template tag and add filter:

# add 5 to forloop.counter {{forloop.counter|add:5}}
# subtract 5 from forloop.counter {{forloop.counter|add:"-5"}}
# devide forloop.counter by 5 {% widthratio forloop.counter 5 1 %}
# multiply forloop.counter by 5 {% widthratio forloop.counter 1 5 %}