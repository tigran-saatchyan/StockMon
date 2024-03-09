from django.urls import reverse_lazy
from django.views import generic
from portfolio.forms import StockPortfolioForm

from portfolio.models import StockPortfolio


class ListView(generic.ListView):
    model = StockPortfolio
    context_object_name = "portfolio_list"


class DetailView(generic.DetailView):
    model = StockPortfolio
    context_object_name = "portfolio"


class CreateView(generic.CreateView):
    model = StockPortfolio
    form_class = StockPortfolioForm
    success_url = reverse_lazy("portfolio:detail-portfolio")


class UpdateView(generic.UpdateView):
    model = StockPortfolio
    form_class = StockPortfolioForm
    success_url = reverse_lazy("portfolio:list-portfolio")


class DeleteView(generic.DeleteView):
    model = StockPortfolio
    success_url = reverse_lazy("portfolio:list-portfolio")
