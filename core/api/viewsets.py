from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter


class PontoTuristicoViewSets(ModelViewSet):
    
    serializer_class = PontoTuristicoSerializer
    
    # habilitando mais buscas no endpoint
    
    filter_backends = [SearchFilter]
    
    # fazendo a busca pelo endereço e mudando o lockup_prefixes
    #  lookup_prefixes = {
    #     '^': 'istartswith',
    #     '=': 'iexact',
    #     '@': 'search',
    #     '$': 'iregex',
    # }
    
    search_fields = ['nome', 'desc', '^endereco__linha1']
    
    def get_queryset(self):
        
        # fazendo filtragem sem django-filter
        
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        desc = self.request.query_params.get('desc', None)
        
        queryset = PontoTuristico.objects.all()
        
        if id:
            queryset = PontoTuristico.objects.filter(id=id)
        if nome:
            
            # '__iexact' faz com que a busca não seja 'case sentitive'
            
            queryset = queryset.PontoTuristico.filter(nome__iexact=nome)
        if desc:
            queryset = queryset.PontoTuristico.filter(desc__iexact=desc)

        return queryset
    
    # SOBRESCRITA DE MÉTODOS PADRÕES
    
    # oque é retornado quando fazemos um GET na API
    # Podemos manipular os resultados sobrescrevendo o método list()
    # ao contrario ele retorna uma lista de todos os itens
    
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSets, self).list(request, *args, **kwargs)
    
    # Create
    
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSets, self).create(request, *args, **kwargs)
    # Delete
    # possivel fazer autenticações e verificar permissões
    
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSets, self).destroy(request, *args, **kwargs)
    
    # retrieve
    # funciona para um GET de um recurso especifico, exemplo: '/pontoturistico/4'
    
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSets, self).retrieve(request, *args, **kwargs)
    
    # # update
    
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSets, self).update(request, *args, **kwargs)
    
    # patch / partial_update
    
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSets, self).partial_update(request, *args, **kwargs)
    
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
    