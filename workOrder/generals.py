from django.contrib.auth.models import User
from workOrder.models import Profile

class Work_order_status():
    SPV_ORG_ACTION = (('op','Open'),
                    ('cl','Close'))

    SPTD_ORG_ACTION = (('ch','Check'),
                    ('rv','Revise'))

    MGR_ORG_ACTION = (('ap','Approve'),
                    ('rc','Re-Check'))

    MGR_EXE_ACTION = ('rw','Review')

    SPTD_EXE_ACTION = (('sc','Schedule'),
                    ('rj','Reject'))

    SPV_EXE_ACTION = (('cm','Complete'),
                    ('ns','Need Shutdown'),
                    ('nm','Need Material'),
                    ('nc','Neen MOC'),
                    ('nr','Need Regulation'),
                    ('ot','Other'))

    FRM_EXE_ACTION = (('','Finish'),
                    ('','Cancel'))

    def __init__(self, user):
        self.user = user

    def getWoStatus(self):
        for g in self.user.groups.all():
            print(f'user groups : {g.name}')
        if g.name == 'ORG_SPV':
            return self.SPV_ORG_ACTION


