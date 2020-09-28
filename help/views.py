from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HelpHomeView(TemplateView):
    template_name = 'help/cmms.html'

class HelpWorkOrderView(TemplateView):
    template_name = 'help/workOrder.html'

class HelpPmPdmView(TemplateView):
    template_name = 'help/PmPdm.html'

class HelpEquipmentView(TemplateView):
    template_name = 'help/equipment.html'

class HelpReportingView(TemplateView):
    template_name = 'help/reporting.html'

class HelpUtilityView(TemplateView):
    template_name = 'help/utility.html'
