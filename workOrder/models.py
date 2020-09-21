from django.db import models

# development password : start1234
# Create your models here.
# https://studygyaan.com/django/how-to-extend-django-user-model#OneToOneLink
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from utility.models import Section, Department, Action, Wo_priority
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

    date_open = models.DateField()
    date_finish = models.DateField(null=True)

    # Foreign Key used because work order can only have one Status, but Status can have multiple work order
    # Status class has already been defined so we can specify the object above.
    status = models.ForeignKey(Action,
        on_delete=models.SET_NULL,
        null=True)

    # Foreign Key used because work order can only have one priority, but priority can have multiple work order
    # Wo_priority class has already been defined so we can specify the object above.
    priority = models.ForeignKey(Wo_priority,
        on_delete=models.SET_NULL,
        null=True)

    current_user_id = models.IntegerField(null=True)
    executor_user_id = models.IntegerField(null=True)

    class Meta:
        ordering = ['originator','status','wo_number']

    def get_absolute_url(self):
        """Returns the url to access a list of work_orders."""
        #"""Returns the url to access a detail record for this work order."""
        return reverse('workOrder:work_order-detail', args=[str(self.id)])
        #return reverse('work_orders')

    def save(self, *args, **kwargs):
        # Do custom logic here (e.g. validation, logging, call third party service)
        # Run default save() method
        super(Work_order,self).save(*args, **kwargs)

    def updateFields(self,**kwargs):
        '''update fields model'''
        print(f'updateFileds=>len(kwargs):{len(kwargs)}')
        print(f'updateFileds=>kwargs.keys():{kwargs.keys()}')
        print(f'updateFileds=>kwargs.values():{kwargs.values()}')
        #self.save(update_fields=['name'])updateExecutorUserId

    def updateStatus(self,fieldVal):
        '''update status field'''
        self.status = fieldVal
        self.save(update_fields=['status'])

    def updateCurrentUserId(self,fieldVal):
        '''update current_user_id field'''
        self.current_user_id = fieldVal
        self.save(update_fields=['current_user_id'])

    def updateExecutorUserId(self,fieldVal):
        '''update executor_user_id field'''
        self.executor_user_id = fieldVal
        self.save(update_fields=['executor_user_id'])

    def updateDateFinish(self,fieldVal):
        '''update executor_user_id field'''
        self.date_finish = fieldVal
        self.save(update_fields=['date_finish'])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.wo_number}'

class Wo_journal(models.Model):
    """Model representing a work order journal"""
    comment = models.CharField(max_length=200, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    
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

    # Foreign Key used because work order can only have one Action, but Action can have multiple work order journal
    # Action class has already been defined so we can specify the object above.
    action = models.ForeignKey(Action,
        on_delete=models.SET_NULL,
        null=True)

    class Meta:
        ordering = ['-date', '-time']

    def get_absolute_url(self):
        """Returns the url to access a list of work_orders."""
        return reverse('workOrder:work_orders')

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.concern_user}'

class Wo_completion(models.Model):
    """Model representing a work order completion"""
    action = models.TextField(max_length=1000, null=True, help_text='Enter action')
    manPower = models.TextField(max_length=100, null=True, help_text='Man power name')
    material = models.TextField(max_length=500, null=True, help_text='Enter material')
    tool = models.TextField(max_length=500, null=True, help_text='Enter action')
    date = models.DateField(null=True)
    duration = models.IntegerField(help_text='Enter duration (hours)', null=True)
    
    # Foreign Key used because Wo_completion can only have one acted_user, but acted_user can have multiple Wo_completion
    # User class has already been defined so we can specify the object above.
    acted_user = models.ForeignKey(User,
        on_delete=models.SET_NULL,
        null=True)

    # Foreign Key used because Wo_completion can only have one wO_completed, but wO_completed can have multiple Wo_completion
    # User class has already been defined so we can specify the object above.
    wO_completed = models.ForeignKey(Work_order,
        on_delete=models.SET_NULL,
        null=True)

    # Foreign Key used because work order can only have one Status, but Status can have multiple work order
    # Status class has already been defined so we can specify the object above.
    status = models.ForeignKey(Action,
        on_delete=models.SET_NULL,
        null=True)

    class Meta:
        ordering = ['date']

    def get_absolute_url(self):
        """Returns the url to access a list of work_orders."""
        return reverse('workOrder:work_orders')

    def __str__(self):
        """String for representing the Model object."""
        return f'Work order completion'

class Wo_instruction(models.Model):
    """Model representing a work order instruction"""
    instruction = models.TextField(max_length=1000, null=True, help_text='Enter action')
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    
    # Foreign Key used because Wo_completion can only have one acted_user, but acted_user can have multiple Wo_completion
    # User class has already been defined so we can specify the object above.
    user = models.ForeignKey(User,
        on_delete=models.SET_NULL,
        null=True)

    # Foreign Key used because Wo_completion can only have one wO_completed, but wO_completed can have multiple Wo_completion
    # User class has already been defined so we can specify the object above.
    work_order = models.ForeignKey(Work_order,
        on_delete=models.SET_NULL,
        null=True)

    def get_absolute_url(self):
        """Returns the url to access a list of work_orders."""
        return reverse('workOrder:work_orders')

    def __str__(self):
        """String for representing the Model object."""
        return f'Work order instruction'

