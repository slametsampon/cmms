from django.shortcuts import render

from workOrder.models import Work_order

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_work_orders = Work_order.objects.all().count()
    
    context = {
        'num_work_orders': num_work_orders,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class Work_orderListView(generic.ListView):
    model = Work_order

class Work_orderDetailView(generic.DetailView):
    model = Work_order

