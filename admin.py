from django.contrib import admin
from hello.models import User,Recruiter,Student

admin.site.register(User)

class RecruiterFilter(admin.ModelAdmin):
    list_display=['username','fname','lname','idno','email','cname','password']
    list_display_links=['idno']
    list_editable=['username','fname','lname','email','cname','password']
    list_filter=['username','email']
admin.site.register(Recruiter,RecruiterFilter)

class StudentFilter(admin.ModelAdmin):
    list_display=['sname','fname','lname','email','iname','pass1']
    list_display_links=['iname']
    list_editable=['sname','fname','lname','email','pass1']
    list_filter=['sname','email']
admin.site.register(Student,StudentFilter)
