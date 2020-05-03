from django.urls import path

from apps.articles.views import main_page, SearchResultsView

app_name = 'articles'

urlpatterns = [
    path('search/', main_page, name='main-page'),
    path('results/', SearchResultsView.as_view(), name='search-results')
]
