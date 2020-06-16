from django.core.cache import cache

from apps.articles.models import Article


def get_articles(search_q, cache_ttl=20):
    akey = f'articles_search-{search_q}'
    articles = cache.get(akey)
    if not articles:
        articles = Article.objects.filter(title__icontains=search_q)
        cache.set(akey, articles, cache_ttl)
    return articles
