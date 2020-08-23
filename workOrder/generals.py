from workOrder.models import User, Profile, Section, Department
from workOrder.models import Work_order

class WoMisc():
    MAX_WO_NBR = 4

    def __init__(self, user):
        self.user = user

        print(f'user : {self.user}')

    def getWoStatus(self, action):
        for g in self.user.groups.all():
            #print(f'user groups : {g.name}')
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

        # Generate counts of some of the main objects
        num_work_orders = Work_order.objects.all().count()
        strWoNbr = str(num_work_orders)
        remain = self.MAX_WO_NBR - len(strWoNbr)

        #put '0' before number
        woNbr = ''
        for i in range(remain):
            woNbr += '0'
        woNbr += strWoNbr

        return (f'{userDept.initial}:{woNbr}')

    def getWoOriginator(self):
        # get user - initial
        userProfile = Profile.objects.get(id=self.user.id)

        return self.user.id
