from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView, FormView

from apps.articles.forms import ArticleImageForm
from apps.articles.models import Article


def main_page(request, some_id=None, *args, **kwargs):
    return render(request, 'pages/main_page.html')


@login_required
def main_page_logged_id(request, some_id=None, *args, **kwargs):
    return render(request, 'pages/main_page.html')


class SearchResultsView(View):
    def get(self, request, **kwargs):
        # form = SearchForm(data=request.GET)
        url = reverse('articles:search-results')
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

    def post(self, request):
        return HttpResponse('{}', status=201)


class ShowTitsView(TemplateView):
    template_name = 'tits_list.html'

    def get_context_data(self, **kwargs):
        # self.request
        return {
            'tits': 2
        }


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tits'] = 42
        return ctx


class ArticleUpdateImageView(FormView):
    form_class = ArticleImageForm
    template_name = 'article_image-update.html'

    def get_success_url(self):
        return reverse('articles:detail', kwargs={'id': self.kwargs['id']})

    def form_valid(self, form):
        # get_object_or_404()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['id'] = self.kwargs['id']

        return ctx
