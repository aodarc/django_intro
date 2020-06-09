from django.urls import path, include

from api.views.articles import ArticleApiView, ArticleGenericView

app_name = 'api'

articles = [
    # path('', ArticleApiView.as_view(), name='list'),
    path('', ArticleGenericView.as_view(), name='list'),
]

urlpatterns = [
    path('articles/', include(articles)),
]
