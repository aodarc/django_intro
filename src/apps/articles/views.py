from django.shortcuts import render
# Create your views here.
from django.views import View

from apps.articles.forms import SearchForm
from apps.articles.models import Article


def main_page(request):
    return render(request, 'pages/main_page.html')


class SearchResultsView(View):
    def get(self, request, **kwargs):
        # form = SearchForm(data=request.GET)
        search_q = request.GET.get('search', '')
        if search_q:
            articles = Article.objects.filter(title__icontains=search_q)
        else:
            articles = Article.objects.all()

        context_data = {
            'articles': articles,
            # 'search_form': form
        }
        return render(request, 'pages/search.html', context=context_data)
