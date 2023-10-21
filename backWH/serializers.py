from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from backWH.models import People

class PeopleSerializer(ModelSerializer):
    class Meta:
        model = People
        fields = "__all__"
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)
        
        
class PeopleDetailSerializer(ModelSerializer):
    class Meta:
        model = People
        fields = "__all__"
        depth = 1
        foto = ImageSerializer(required=False)

class PeopleListSerializer(ModelSerializer):
    class Meta:
        model = People
        fields = ["id", "nome", "servico", "local", "idade", "valor", "foto"]