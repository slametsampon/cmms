from django.db import models

# development password : start1234
# Create your models here.
# https://studygyaan.com/django/how-to-extend-django-user-model#OneToOneLink
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nik = models.IntegerField(null=True)
    initial = models.CharField(max_length=3, null=True)
    approver = models.CharField(max_length=3, null=True)
    # Foreign Key used because user can only have one section, but section can have multiple users
    # Section as a string rather than object because it hasn't been declared yet in the file
    section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
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
        return self.initial

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
        return self.initial

#models for Work order 

class Work_order_journal(models.Model):
    """Model representing a work order journal"""
    prev_user = models.CharField(max_length=3, null=True)
    next_user = models.CharField(max_length=3, null=True)

    comment = models.CharField(max_length=200, null=True, help_text='Enter comment')
    date = models.DateField()
    
    class Meta:
        ordering = ['date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.prev_user} => {self.next_user}'

class Work_order_completion(models.Model):
    """Model representing a work order completion"""
    action = models.TextField(max_length=1000, null=True, help_text='Enter action')
    manPower = models.CharField(max_length=100, null=True, help_text='Man power name')
    material = models.TextField(max_length=1000, null=True, help_text='Enter material')
    tool = models.TextField(max_length=1000, null=True, help_text='Enter action')
    date = models.DateField(null=True)
    duration = models.IntegerField(help_text='Enter duration (hours)', null=True)
    
    class Meta:
        ordering = ['date']

    def __str__(self):
        """String for representing the Model object."""
        return f'Work order cmpletion'

class Work_order(models.Model):
    """Model representing a work order"""
    wo_number = models.CharField(max_length=20, null=True, help_text='Enter tagnumber(Prodxxxx)')
    tagnumber = models.CharField(max_length=50, null=True, help_text='Enter tagnumber(eg. FT-1405)')
    problem = models.TextField(max_length=1000, null=True, help_text='Enter problem')

    # Foreign Key used because work order can only have one originator, but originator can have multiple work order
    # User class has already been defined so we can specify the object above.
    originator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    
    # Foreign Key used because work order can only have one dest_section, but dest_section can have multiple work order
    # User class has already been defined so we can specify the object above.
    dest_section = models.ForeignKey(Section,
        on_delete=models.SET_NULL,
        null=True,
        help_text = 'Select destination section')

    PRIORITY_STATUS = (
        ('n', 'Normal'),
        ('e', 'Emergency'),
        ('s', 'Shutdown'),
        ('o', 'Other'),
    )

    priority = models.CharField(max_length=1,
        choices=PRIORITY_STATUS,
        blank=True,
        default='n',
        help_text = 'Select priority')

    date_open = models.DateField()

    status = models.CharField(max_length=20,
        blank=True)
    
    class Meta:
        ordering = ['originator','status','wo_number']

    def get_absolute_url(self):
        """Returns the url to access a detail record for this work order."""
        return reverse('Work_order-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'Work order cmpletion'