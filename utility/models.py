# development password : start1234
# Create your models here.
# https://studygyaan.com/django/how-to-extend-django-user-model#OneToOneLink
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from workOrder.models import Status

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forward_path = models.IntegerField(null=True)
    reverse_path = models.IntegerField(null=True)

    # ManyToManyField used because Status can contain many ProfileUtilities. ProfileUtilities can cover many Statuses.
    # Status class has already been defined so we can specify the object above.
    actions = models.ManyToManyField(Status, help_text='Select actions')

    # Foreign Key used because user can only have one section, but section can have multiple users
    # Section as a string rather than object because it hasn't been declared yet in the file
    section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True)

    @classmethod
    def update_or_create_dict(cls,dtDict):

        #insert User
        dtDict['user'] = User.objects.get(username = dtDict.get('username'))
        #remove key username
        dtDict.pop('username')

        #insert section
        dtDict['section'] = Section.objects.get(name = dtDict.get('foreign_section'))
        #remove key foreign_section
        dtDict.pop('foreign_section')

        #update from name to id
        usr = None
        if dtDict.get('forward_path'):
            usr = User.objects.get(username = dtDict.get('forward_path'))
        dtDict['forward_path'] = usr.id

        #update from name to id
        usr = None
        if dtDict.get('reverse_path'):
            usr = User.objects.get(username = dtDict.get('reverse_path'))
        dtDict['reverse_path'] = usr.id

        #get first key for unique key
        k=None
        for k,v in dtDict.items():
            if k:
                break
        
        #user as unique value, kindly modify as needed
        return cls.objects.update_or_create(
            user=dtDict.get('user'),
            defaults=dtDict,
        )            

    @classmethod
    def update_or_create_action_dict(cls,dtDict):
        #insert User
        user = User.objects.get(username = dtDict.get('username'))
        userProfile = Profile.objects.get(user = user)

        #get action
        act = Status.objects.get(name=dtDict.get('action'))

        #add action to user profile
        userProfile.actions.add(act)
        userProfile.save()

@receiver(post_save, sender=User)
def create_user_Profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_Profile(sender, instance, **kwargs):
    instance.profile.save()

class Section(models.Model):
    """Model representing a section of organization"""
    name = models.CharField(max_length=50, null=True, help_text='Enter name of section(eg. Electrical & Instrumentation)')
    description = models.CharField(max_length=200, null=True, help_text='Enter description of section')
    # Foreign Key used because section can only have one department, but department can have multiple sections
    # Section as a string rather than object because it hasn't been declared yet in the file
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['department','name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    @classmethod
    def update_or_create_dict(cls,dtDict):

        #get dept object
        depName = dtDict.get('foreign_department')
        dept = Department.objects.get(name = depName)

        #remove key foreign_department
        dtDict.pop('foreign_department')

        #insert Department
        dtDict['department']=dept

        #get first key for unique key
        k=None
        for k,v in dtDict.items():
            if k:
                break
        
        #name as unique value, kindly modify as needed
        return cls.objects.update_or_create(
            name=v,
            defaults=dtDict,
        )            

class Department(models.Model):
    """Model representing a department of organization"""
    name = models.CharField(max_length=50, null=True, help_text='Enter name of section(eg. Maintenance)')
    #initial = models.CharField(max_length=5, null=True, help_text='Enter initial of section(eg. Mntc)')
    description = models.CharField(max_length=200, null=True, help_text='Enter description of department')
    
    class Meta:
        ordering = ['name']


    def __str__(self):
        """String for representing the Model object."""
        return self.name

    @classmethod
    def update_or_create_dict(cls,dtDict):

        #get first key for unique key
        k=None
        for k,v in dtDict.items():
            if k:
                break
        
        #name as unique value, kindly modify as needed
        return cls.objects.update_or_create(
            name=v,
            defaults=dtDict,
        )            
