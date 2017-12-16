from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Company, Department


class IndexView(generic.ListView):
    template_name = 'expense/index.html'
    context_object_name = 'company_list'

    def get_queryset(self):
        """Return the last five published Companys."""
        return Company.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Company
    template_name = 'expense/detail.html'


class ResultsView(generic.DetailView):
    model = Company
    template_name = 'expense/results.html'

def select(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    try:
        selected_department = company.department_set.get(pk=request.POST['department'])
    except (KeyError, Department.DoesNotExist):
        # Redisplay the company voting form.
        return render(request, 'expense/detail.html', {
            'company': company,
            'error_message': "You didn't select a department.",
        })
    else:
        selected_department.selection += 1
        selected_department.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('expense:results', args=(company.id,)))