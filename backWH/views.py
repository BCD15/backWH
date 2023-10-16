from rest_framework.viewsets import ModelViewSet

from backWH.models import People
from backWH.serializers import PeopleSerializer, PeopleDetailSerializer, PeopleListSerializer

class PeopleViewSet(ModelViewSet):
    queryset = People.objects.all()
    
    def get_serializer_class(self):
        if self.action == "list":
            return PeopleListSerializer
        elif self.action == "retrieve":
            return PeopleDetailSerializer
        return PeopleSerializer