from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from kitaplar.api.serializers import KitapSerializer, YorumSerializer
from kitaplar.models import Kitap

class KitapListCreateAPI(GenericAPIView):
    
    queryset = Kitap.objects.all()
    serializer_class =KitapSerializer
    #Listelemek
    def get(self, request, *args, **kwargs):
        return self,list(request, *args, **kwargs)