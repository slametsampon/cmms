import datetime
from workOrder.models import User, Profile, Section, Department
from workOrder.models import Work_order, Work_order_journal, Work_order_completion

class WoMisc():
    MAX_WO_NBR = 4

    def __init__(self, user):
        self.user = user

    def getWoStatus(self, action):
        for g in self.user.groups.all():
            status = 'ot' #other

            #originator supervisor
            if 'ORG_SPV' == g.name:
                if action == 'f': #forward action
                    status = 'op' # Open
                elif action == 'c': #close
                    status = 'cl' #Close

            #originator superintendent
            if 'ORG_SPTD' == g.name:
                if action == 'f': #forward action
                    status = 'ck' # Check
                elif action == 'r': #return
                    status = 'rv' #Revise

            #originator manager
            if 'ORG_MGR' == g.name:
                if action == 'f': #forward action
                    status = 'ap' # Approve
                elif action == 'r': #return
                    status = 'rc' #Re-check

            #executor manager
            if 'EXC_MGR' == g.name:
                if action == 'f': #forward action
                    status = 'rw' # Review
                elif action == 'r': #return
                    status = 'rj' #Reject

            #executor superintendent
            if 'EXC_SPTD' == g.name:
                if action == 'f': #forward action
                    status = 'sc' # Schedule
                elif action == 'r': #return
                    status = 'rt' #Return
                elif action == 's': #Shutdown
                    status = 'ns' #Need Shutdown
                elif action == 'l': #Need Material
                    status = 'nl' #Need Materials
                elif action == 'm': #Need MOC
                    status = 'nm' #Need MOC
                elif action == 'o': #Other
                    status = 'ot' #Need Regulation, etc

            #executor supervisor
            if 'EXC_SPV' == g.name:
                if action == 'f': #forward action
                    status = 'ec' # Execute
                elif action == 'r': #return
                    status = 'rt' #Return
                elif action == 't': #complete
                    status = 'cm' #Complete

            #executor foreman
            if 'EXC_FRM' == g.name:
                if action == 'h': #finish action
                    status = 'fn' # Finish
                elif action == 'i': #in progress
                    status = 'ip' #in progress
                elif action == 'r': #return
                    status = 'cn' #Cancel

            return status

    def getWoNumber(self):
        # get user department - initial
        userProfile = Profile.objects.get(id=self.user.id)
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

    def getCurrentUser(self, action):
        pendingList = ["s", "l", "m", "o"] #Shutdown, Need Material, MOC, Other
        # get user - approver
        userProfile = Profile.objects.get(id=self.user.id)

        currentUserId = self.user.id

        #role for general user
        if action in pendingList:
            currentUserId = self.user.id
        elif action == 'f': #forward action
            currentUserId = Profile.objects.get(initial=userProfile.forward_path).id
        elif action == 'r': #return
            currentUserId = Profile.objects.get(initial=userProfile.reverse_path).id

        #role for foreman executor
        for g in self.user.groups.all():

            #Executor Foreman
            if 'EXC_FRM' == g.name:
                if action == 'h': #finish action
                    currentUserId = Profile.objects.get(initial=userProfile.reverse_path).id

                elif action == 'i': #in progress action
                    currentUserId = self.user.id

        #role during off hour, by pass mode
        if not(self.__isOfficeWorkingHour()): 
            for g in self.user.groups.all():
                #originator supervisor
                if 'ORG_SPV' == g.name:
                    if action == 'f': #forward action
                        currentUserId = self.__getForemanExecutorId()

        currentUser = User.objects.get(id=currentUserId)
        return currentUser

    def woInitJournal(self):
        # get user - woOnProcess and update 
        woOnProcess = Work_order.objects.get(id=self.num_work_orders)

        #To create and save an object in a single step, use the create() method.
        comment = 'Opening with bypass mode'
        if self.__isOfficeWorkingHour():
            comment = 'Opening with normal mode'
        woJournal = Work_order_journal.objects.create(
            comment=comment,
            action='f',#forward
            concern_user=self.user,
            wO_on_process=woOnProcess,
            date=datetime.date.today(),
            time=datetime.datetime.now().time()
            )

    def woOnCurrentUser(self):
        # get list of WO on concern in journal myModel.field_object
        woListId=[]
        woList = Work_order.objects.filter(current_user_id=self.user.id)
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
                if 'EXC_FRM' == g.name:
                    return usr.id 
    
