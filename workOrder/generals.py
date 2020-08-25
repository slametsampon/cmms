import datetime
from workOrder.models import User, Profile, Section, Department
from workOrder.models import Work_order, Work_order_journal, Work_order_completion

class WoMisc():
    MAX_WO_NBR = 4

    def __init__(self, user):
        self.user = user

    def getWoStatus(self, action):
        for g in self.user.groups.all():
            if 'ORG_SPV' == g.name:
                if action == 'f': #forward action
                    return 'op' # Open
                elif action == 'r': #return
                    return 'cl' #Close
                else :
                    return action
            else:
                return 'ot' #other

    def getWoNumber(self):
        # get user department - initial
        userProfile = Profile.objects.get(id=self.user.id)
        userSection = Section.objects.get(id=userProfile.section.id)
        userDept = Department.objects.get(id=userSection.department.id)

        # Generate num_work_orders of some of the main objects
        self.num_work_orders = Work_order.objects.order_by('id').last().id+1

        strWoNbr = str(self.num_work_orders)
        remain = self.MAX_WO_NBR - len(strWoNbr)

        #put '0' before number
        woNbr = ''
        for i in range(remain):
            woNbr += '0'
        woNbr += strWoNbr

        return (f'{userDept.initial}/{woNbr}')

    def woForwarder(self):
        # get user - approver
        userProfile = Profile.objects.get(id=self.user.id)
        userApproverId = Profile.objects.get(initial=userProfile.approver).id
        userApprover = User.objects.get(id=userApproverId)

        # get user - woOnProcess and update 
        self.woOnProcess = Work_order.objects.get(id=self.num_work_orders)
        woOnProcess = self.woOnProcess
        woOnProcess.current_user_id = userApproverId
        woOnProcess.save()

        #To create and save an object in a single step, use the create() method.
        woJournal = Work_order_journal.objects.create(comment='Opening work order',
            action='f',#forward
            concern_user=userApprover,
            wO_on_process=woOnProcess,
            date=datetime.date.today())

    def woOnCurrentUser(self):
        # get list of WO on concern in journal myModel.field_object
        woListId=[]
        woList = Work_order.objects.filter(current_user_id=self.user.id)
        for wo in woList:
            woListId.append(wo.id)
        return woListId
