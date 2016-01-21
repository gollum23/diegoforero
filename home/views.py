from django.views.generic import TemplateView, ListView

from .models import PortfolioItem


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        portfolio_items = PortfolioItem.objects.filter(published=True).order_by('-order')
        context['portfolio'] = portfolio_items
        return context
