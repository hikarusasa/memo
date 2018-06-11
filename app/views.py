from django.views import generic
from django.urls import reverse_lazy
from .models import Description
from .forms import SearchForm,TextCreateForm
# Create your views here.


class IndexView(generic.ListView):
    model = Description
    paginate_by = 3

    def get_context_data(self):
        """create the dictionary sending to template"""
        context = super().get_context_data()
        context['form'] = SearchForm(self.request.GET)  # add form in the original dictionary
        return context

    def get_queryset(self):
        # create [employee_list] sending to template
        form = SearchForm(self.request.GET)
        form.is_valid() # if this is not, cannot execute cleaned_data

        # firstly, get all
        queryset = super().get_queryset()

        # filter by category if there is a selections of department
        category = form.cleaned_data['category']
        if category:
            queryset = queryset.filter(category=category)
        return queryset

class AddView(generic.CreateView):
    model = Description
    form_class = TextCreateForm
    success_url = reverse_lazy('memo:index')

class DeleteView(generic.DeleteView):
    model = Description
    success_url = reverse_lazy('memo:index')

class DetailView(generic.DetailView):
    model = Description
