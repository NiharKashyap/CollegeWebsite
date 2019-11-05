from django.contrib import admin
from .models import users, Feedback, StuDetails
# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = ('uname' , 'pword')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('cmnt', 'rating')

class StuDetailsAdmin(admin.ModelAdmin):
    list_display = ('uname', 'fname' , 'semester', 'department', 'roll_no', 'verified')

admin.site.register(users, UsersAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(StuDetails, StuDetailsAdmin)