from django.contrib import admin

from .models import Section, Department, ProfileUtility
from .forms import ProfileForm
from django.forms import Select

# Register your models here.
# Register the Admin classes for Department using the decorator
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    list_filter = ('name','description')

# Register the Admin classes for Section using the decorator
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
        
# Register the Admin classes for Section using the decorator
@admin.register(ProfileUtility)
class ProfileUtilityAdmin(admin.ModelAdmin):
    form = ProfileForm
    list_display = ('user','section','forward_path', 'reverse_path')
    list_filter = ('section', 'user')
    fieldsets = (
        (None, {
            'fields': ('user',  'section')
        }),
        ('Approval Path', {
            'fields': ('forward_path', 'reverse_path', 'action')
        }),
    )
    
