from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from backWH.models import People

class PeopleSerializer(ModelSerializer):
    class Meta:
        model = People
        fields = "__all__"
        depth = 1
        capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
        
class PeopleDetailSerializer(ModelSerializer):
    class Meta:
        model = People
        fields = "__all__"
        depth = 1
        capa = ImageSerializer(required=False)

class PeopleListSerializer(ModelSerializer):
    class Meta:
        model = People
        fields = ["id", "titulo", "preco"] 