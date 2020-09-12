# development password : start1234
# Create your models here.
# https://studygyaan.com/django/how-to-extend-django-user-model#OneToOneLink
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from workOrder.models import Status

class ProfileUtility(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nik = models.IntegerField(null=True)
    initial = models.CharField(max_length=3, null=True)
    forward_path = models.CharField(max_length=3, null=True)
    reverse_path = models.CharField(max_length=3, null=True)

    # ManyToManyField used because Status can contain many ProfileUtilities. ProfileUtilities can cover many Statuses.
    # Status class has already been defined so we can specify the object above.
    action = models.ManyToManyField(Status, help_text='Select actions')

    # Foreign Key used because user can only have one section, but section can have multiple users
    # Section as a string rather than object because it hasn't been declared yet in the file
    section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True)

@receiver(post_save, sender=User)
def create_user_profileUtility(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profileUtility(sender, instance, **kwargs):
    instance.profile.save()

class Section(models.Model):
    """Model representing a section of organization"""
    name = models.CharField(max_length=50, null=True, help_text='Enter name of section(eg. Electrical & Instrumentation)')
    initial = models.CharField(max_length=5, null=True, help_text='Enter initial of section(eg. Elins)')
    description = models.CharField(max_length=200, null=True, help_text='Enter description of section')
    # Foreign Key used because section can only have one department, but department can have multiple sections
    # Section as a string rather than object because it hasn't been declared yet in the file
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['department','name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Department(models.Model):
    """Model representing a department of organization"""
    name = models.CharField(max_length=50, null=True, help_text='Enter name of section(eg. Maintenance)')
    initial = models.CharField(max_length=5, null=True, help_text='Enter initial of section(eg. Mntc)')
    description = models.CharField(max_length=200, null=True, help_text='Enter description of department')
    
    ROLE_STATUS = (
        ('e', 'Executor'),
        ('o', 'Originator'),
        ('a', 'Any'),
    )

    role = models.CharField(max_length=1,
        choices=ROLE_STATUS,
        blank=True,
        default='o',
        help_text = 'Select role')

    class Meta:
        ordering = ['name']


    def __str__(self):
        """String for representing the Model object."""
        return self.name
