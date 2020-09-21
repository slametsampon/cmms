from django.contrib import admin

from .models import Section, Department, Profile, Action, Mode, Wo_priority
from .forms import ProfileForm
from django.forms import Select

# Register your models here.

# Register the Admin classes for Section using the decorator
@admin.register(Wo_priority)
class Wo_priorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
        
# Register the Admin classes for Department using the decorator
@admin.register(Mode)
class ModeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

# Register the Admin classes for Department using the decorator
@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('name','mode','description')
    list_filter = ('name','mode','description')

# Register the Admin classes for Department using the decorator
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'initial','description')
    list_filter = ('name', 'initial','description')

# Register the Admin classes for Section using the decorator
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
        
# Register the Admin classes for Section using the decorator
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    list_display = ('user','section','forward_path', 'reverse_path', 'actions')
    list_filter = ('section', 'user')
    fieldsets = (
        (None, {
            'fields': ('user',  'section')
        }),
        ('Approval Path', {
            'fields': ('forward_path', 'reverse_path', 'actions')
        }),
    )
    
