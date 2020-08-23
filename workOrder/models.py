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

#models for Work order 


from django.urls import reverse
class Work_order(models.Model):
    """Model representing a work order"""
    wo_number = models.CharField(max_length=20, null=True)
    tagnumber = models.CharField(max_length=50, null=True, help_text='Enter tagnumber(eg. FT-1405)')
    problem = models.TextField(max_length=1000, null=True)

    # Foreign Key used because work order can only have one originator, but originator can have multiple work order
    # User class has already been defined so we can specify the object above.
    originator = models.ForeignKey(User,
        on_delete=models.SET_NULL,
        null=True)
    
    # Foreign Key used because work order can only have one dest_section, but dest_section can have multiple work order
    # User class has already been defined so we can specify the object above.
    dest_section = models.ForeignKey(Section,
        on_delete=models.SET_NULL,
        null=True)

    PRIORITY_STATUS = (
        ('n', 'Normal'),
        ('e', 'Emergency'),
        ('s', 'Shutdown'),
        ('o', 'Other'),
    )

    priority = models.CharField(max_length=1,
        choices=PRIORITY_STATUS,
        blank=True,
        default='n')

    date_open = models.DateField()

    ACTION_STATUS = (
        ('f', 'Forward'),
        ('r', 'Return'),
        ('o', 'Other'),
    )

    action = models.CharField(max_length=1,
        choices=ACTION_STATUS,
        blank=True,
        default='f')

    status = models.CharField(max_length=2,
        blank=True)
    
    class Meta:
        ordering = ['originator','status','wo_number']

    def get_absolute_url(self):
        """Returns the url to access a detail record for this work order."""
        return reverse('work_order-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'Work order completion'

class Work_order_journal(models.Model):
    """Model representing a work order journal"""
    comment = models.CharField(max_length=200, null=True, help_text='Enter comment')
    date = models.DateField()
    
    # Foreign Key used because Work_order_journal can only have one concern_user, but Work_order_journal can have multiple concern_user
    # User class has already been defined so we can specify the object above.
    concern_user = models.ForeignKey(User,
        on_delete=models.SET_NULL,
        null=True)
    
    # Foreign Key used because Work_order_journal can only have one wO_on_process, but wO_on_process can have multiple Work_order_journal
    # User class has already been defined so we can specify the object above.
    wO_on_process = models.ForeignKey(Work_order,
        on_delete=models.SET_NULL,
        null=True)

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
    
    # Foreign Key used because Work_order_completion can only have one acted_user, but acted_user can have multiple Work_order_completion
    # User class has already been defined so we can specify the object above.
    acted_user = models.ForeignKey(User,
        on_delete=models.SET_NULL,
        null=True)

    # Foreign Key used because Work_order_completion can only have one wO_completed, but wO_completed can have multiple Work_order_completion
    # User class has already been defined so we can specify the object above.
    wO_completed = models.ForeignKey(Work_order,
        on_delete=models.SET_NULL,
        null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        """String for representing the Model object."""
        return f'Work order cmpletion'
