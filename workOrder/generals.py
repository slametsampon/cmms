from django.contrib.auth.models import User

from workOrder.models import Work_order, Wo_journal, Wo_completion
from utility.models import Profile, Section, Department, Action

import datetime

class WoMisc():
    MAX_WO_NBR = 4

    def __init__(self, user):
        self.user = user

    def getWoNumber(self):
        # get user department - initial

        userProfile = Profile.objects.get(user=self.user)
        userSection = Section.objects.get(id=userProfile.section.id)
        userDept = Department.objects.get(id=userSection.department.id)

        # Generate num_work_orders of some of the main objects
        self.num_work_orders = 1
        if Work_order.objects.all().count():
            self.num_work_orders = Work_order.objects.order_by('id').last().id+1

        strWoNbr = str(self.num_work_orders)
        remain = self.MAX_WO_NBR - len(strWoNbr)

        #put '0' before number
        woNbr = ''
        for i in range(remain):
            woNbr += '0'
        woNbr += strWoNbr

        return (f'{userDept.initial}/{woNbr}')

    def get_next_user(self, act_id):
        '''get next user after action of current user'''
        # get user - approver
        userProfile = Profile.objects.get(user=self.user)

        next_user_id = self.user.id

        #for human readable
        action = Action.objects.get(id = act_id)
        action_mode = action.mode.name

        #role for general user
        if action_mode == 'Reverse':
            next_user_id = Profile.objects.get(user=self.user).reverse_path
        elif action_mode == 'Forward': #forward action
            next_user_id = Profile.objects.get(user=self.user).forward_path
        else: #Stay action
            next_user_id = self.user.id

        #role during off hour, by pass mode
        if not(self.__isOfficeWorkingHour()): 
            for g in self.user.groups.all():
                #originator supervisor
                if 'SPV_ORG' == g.name:
                    if action_mode == 'Forward': #forward action
                        next_user_id = self.__getForemanExecutorId()

        next_user = User.objects.get(id=next_user_id)
        return next_user

    def woInitJournal(self):
        # get user - woOnProcess and update 
        woOnProcess = Work_order.objects.get(id=self.num_work_orders)

        #it just opening
        act = Action.objects.get(name='Open')

        #To create and save an object in a single step, use the create() method.
        comment = 'Opening with bypass mode'
        if self.__isOfficeWorkingHour():
            comment = 'Opening with normal mode'
        woJournal = Wo_journal.objects.create(
            comment=comment,
            action=act,#Open, just opening
            concern_user=self.user,
            work_order=woOnProcess,
            date=datetime.date.today(),
            time=datetime.datetime.now().time()
            )

    def woOnCurrentUser(self):
        # get list of WO on concern in journal myModel.field_object
        woListId=[]
        woList = Work_order.objects.filter(current_user_id=self.user.id)

        #special for originator supervisor
        for g in self.user.groups.all():
            if 'SPV_ORG' == g.name:
                woList = Work_order.objects.filter(current_user_id=self.user.id
                    ).exclude(status=Action.objects.get(name='Close'))
        
        for wo in woList:
            woListId.append(wo.id)
        return woListId

    def __isOfficeWorkingHour(self):
        x = datetime.datetime.now()
        startWorkingHr = datetime.time(8,0,0)
        endWorkingHr = datetime.time(17,0,0)
        currentTime = x.time()
        currentDay = x.strftime('%A')

        if currentDay in ['Saturday','Sunday']:
            return False
        elif currentTime < startWorkingHr or currentTime > endWorkingHr:
            return False
        else: 
            return True

    def __getForemanExecutorId(self):
        for usr in User.objects.all():
            for g in usr.groups.all():
                if 'FRM_EXE' == g.name:
                    return usr.id 
    
