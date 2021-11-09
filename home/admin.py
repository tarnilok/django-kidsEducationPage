from django.contrib import admin
from .models import Contact, Branch, Teacher

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone_number',
        'email',
        'message',
        'created_date'
    )
    
    list_filter = ('name',)
    search_fields = ('name__startswith',)

admin.site.register(Contact, ContactAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'phone_teacher',
        'email_teacher',
        'speciality',
        'image',
        'created_date',
        'update_date'
    )
    
    list_filter = ('first_name',)
    search_fields = ('first_name__startswith',)

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Branch)


