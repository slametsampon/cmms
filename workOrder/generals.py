from workOrder.models import User, Profile

class WoMisc():

    def __init__(self, user):
        usersCmp = User.objects.all().select_related('profile')

        self.user = user
        print(f'user : {self.user}')
        print(f'user : {self.user.username}')

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



