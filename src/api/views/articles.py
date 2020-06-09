from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from api.serializers.v1.article import ArticleSerializer, ArticleModelSerializer
from apps.articles.models import Article


class ArticleApiView(APIView):
    def get(self, request, **kwargs):
        serializer = ArticleModelSerializer(instance=Article.objects.last())
        return Response(serializer.data)

    def post(self, request, **kwargs):
        serializer = ArticleModelSerializer(data=request.data)

        if serializer.is_valid():
            article = serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
