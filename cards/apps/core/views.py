from django.http import request
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView, TemplateView

from .forms import ExpenseForm
from .models import Card


class IndexView(TemplateView):

    template_name = 'core/index.html'
    extra_context = {'title': 'Cards'}


class CardListView(ListView):

    model = Card
    context_object_name = 'cards'
    templtae_name = 'cards/card_list.html'


class CardDetailView(DetailView):

    model = Card
    context_object_name = 'card'
    template_name = 'core/card_detail.html'


class ExpenseFormView(FormView):

    form_class = ExpenseForm
    success_url = reverse_lazy('expense-result')
    template_name = 'core/expense_form.html'


class ExpenseResultsView(TemplateView):

    template_name = 'core/expense_results.html'

    def get_context_data(self, **kwargs):
        kwargs.update({'cards': Card.objects.all().order_by('name')})
        return super().get_context_data(**kwargs)
