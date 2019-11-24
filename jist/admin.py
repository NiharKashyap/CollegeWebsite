from django.contrib import admin
from .models import users, Feedback, StuDetails
from django.contrib.auth.models import User, Group

# Register your models here.
admin.site.site_header= "Welcome Admin"
admin.site.index_title = "Welcome to JIST Admin Panel"

class UsersAdmin(admin.ModelAdmin):
    list_display = ('uname' , 'pword')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('cmnt', 'rating')

class StuDetailsAdmin(admin.ModelAdmin):
    list_display = ('uname', 'fname' , 'semester', 'department', 'roll_no', 'verified')


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(users, UsersAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(StuDetails, StuDetailsAdmin)