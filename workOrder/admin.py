from django.contrib import admin
from .models import Section, Department, Work_order, Work_order_completion, Work_order_journal, Profile

# Register your models here.
# Register the Admin classes for Department using the decorator
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')

# Register the Admin classes for Section using the decorator
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'initial')
    
# Register the Admin classes for Section using the decorator
@admin.register(Work_order_journal)
class Work_order_journalAdmin(admin.ModelAdmin):
    pass
    
# Register the Admin classes for Section using the decorator
@admin.register(Profile)
class Work_order_journalAdmin(admin.ModelAdmin):
    pass
    
