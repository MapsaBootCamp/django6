from rest_framework import serializers
from django.utils.timezone import now

from magazine.models import Magazine


class MagazineListSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    ghedmat = serializers.SerializerMethodField()

    class Meta:
        model = Magazine
        fields = ("url", "name", "number", "category", "ghedmat")
        extra_kwargs = {"url": {"lookup_field": "slug"}}
    
    def get_ghedmat(self, obj):
        print(now().date())
        return (now().date() - obj.created_date).days


class MagazineDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Magazine
        fields = ("name", "number", "content")


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField()