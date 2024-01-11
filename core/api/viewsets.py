from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class PontoTuristicoViewSets(ModelViewSet):
    
    serializer_class = PontoTuristicoSerializer
    
    def get_queryset(self):
        
        return PontoTuristico.objects.filter(aprovado=True)
    
    # SOBRESCRITA DE MÉTODOS PADRÕES
    
    # oque é retornado quando fazemos um GET na API
    # Podemos manipular os resultados sobrescrevendo o método list()
    # ao contrario ele retorna uma lista de todos os itens
    
    # def list(self, request, *args, **kwargs):
    #     return Response({'teste': 123})
    
    # Create
    
    # def create(self, request, *args, **kwargs):
    #     return Response({'hello': request.data['nome']})

    # Delete
    # possivel fazer autenticações e verificar permissões
    
    # def destroy(self, request, *args, **kwargs):
    #     pass
    
    # retrieve
    # funciona para um GET de um recurso especifico, exemplo: '/pontoturistico/4'
    
    # def retrieve(self, request, *args, **kwargs):
    #     pass
    
    # # update
    
    # def update(self, request, *args, **kwargs):
    #     pass
    
    # patch / partial_update
    
    # def partial_update(self, request, *args, **kwargs):
    #     pass
    
    # ACTIONS
    # método para caso deseje denunciar um ponto turistico
    # para um recurso especifico '/pontoturistico/4/denunciar'
    
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass
    
    # Para o endpoint inteiro
    # seria possivel fazer uma função para deletar todos os itens de um endpoint
    
    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass