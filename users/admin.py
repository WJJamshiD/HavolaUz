from django.contrib import admin
from .models import User
# Register your models here.




class UserAdmin(admin.ModelAdmin):
    # fields = ['first_name', 'last_name', 'is_staff', 'password']
    fieldsets = (
        ('Personal Information', {
            "fields": (
                ('first_name', 'last_name'),
            ),
        }),
        ('Credentials', {
            "fields": (
                'email', 'password'
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_staff', 'is_superuser'
            ),
            'classes': ('collapse',),
        }),
    )
    
    list_display = ['id', 'first_name', 'last_name']
    list_editable = ['last_name']
    list_display_links = ['first_name']
    readonly_fields = ['password']


admin.site.register(User, UserAdmin)
