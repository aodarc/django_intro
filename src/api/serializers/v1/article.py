from rest_framework import serializers

from apps.articles.models import Article, Tag


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    created_at = serializers.DateTimeField()


class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleModelSerializer(serializers.ModelSerializer):
    tags_ids = serializers.ListSerializer(child=serializers.IntegerField(), write_only=True)
    tags = TagModelSerializer(many=True)

    tag_names = serializers.SerializerMethodField()  # method_name='custom_method_name'

    class Meta:
        model = Article
        fields = ['title', 'body', 'author', 'tags_ids', 'tag_names', 'tags']
        # exclude = []

    def get_tag_names(self, obj: Article) -> str:
        return ', '.join(obj.tags.all().values_list('name', flat=True))

    def validate_tags_ids(self, value):
        # raise ValidationError()
        return Tag.objects.filter(id__in=value)

    def validate(self, attrs):
        return attrs

    def create(self, validated_data: dict) -> dict:
        data = validated_data.copy()
        tags = data.pop('tags_ids')
        article = super().create(data)

        article.tags.add(*tags)

        return article
