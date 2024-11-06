from typing import Any
from django.views.generic import TemplateView

from articles.models import Article

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        last_update_article = Article.objects.order_by('-updated_at').first()
        context['last_updated_article'] = last_update_article
        return context