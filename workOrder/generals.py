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
                elif action == 'r': #return
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

            #executor supervisor
            if 'EXC_SPV' == g.name:
                if action == 'f': #forward action
                    status = 'ec' # Execute
                elif action == 'r': #return
                    status = 'rt' #Reject

            #executor foreman
            if 'EXC_FRM' == g.name:
                if action == 'f': #forward action
                    status = 'fn' # Finish
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
        # get user - approver
        userProfile = Profile.objects.get(id=self.user.id)

        if action == 'f': #forward action
            currentUserId = Profile.objects.get(initial=userProfile.forward_path).id
        elif action == 'r': #return
            currentUserId = Profile.objects.get(initial=userProfile.reverse_path).id
        currentUser = User.objects.get(id=currentUserId)

        return currentUser

    def woInitJournal(self):
        # get user - woOnProcess and update 
        woOnProcess = Work_order.objects.get(id=self.num_work_orders)

        #To create and save an object in a single step, use the create() method.
        woJournal = Work_order_journal.objects.create(comment='Opening work order',
            action='f',#forward
            concern_user=self.user,
            wO_on_process=woOnProcess,
            date=datetime.date.today(),
            time=datetime.date.today().time())

    def woOnCurrentUser(self):
        # get list of WO on concern in journal myModel.field_object
        woListId=[]
        woList = Work_order.objects.filter(current_user_id=self.user.id)
        for wo in woList:
            woListId.append(wo.id)
        return woListId
