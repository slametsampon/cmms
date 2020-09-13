from django.contrib import admin
from .models import Status

# Register your models here.
# Register the Admin classes for Status using the decorator
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):    
    list_display = ('name','description')
    list_filter = ('name','description')
