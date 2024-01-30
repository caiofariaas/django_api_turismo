from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication


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
    
    search_fields = ['^nome', '^desc', '^endereco__linha1']
    
    # o 'lookup_field' é o valor de busca, no caso, ele vem como padrão sendo o 'id' do item
    # mas é possivel alterado apenas sobreescrevento!
    # precisa ser 'UNICO' no banco de dados.
    # ele identifica apenas 1 objeto
    
    # lookup_field =  'nome'
    
    
    # https://www.django-rest-framework.org/api-guide/permissions/
    
    # 'permission_classes' permite você setar permissões para cada endPoint
    # no caso estamos pedindo que o usuário no minimo esteja autenticado.
    
    # AllowAny - permitirá acesso irrestrito
    
    # IsAuthenticated - Vai negar acesso a qualquer usuário não autenticado
    
    # IsAdminUser - vai negar acesso a qualquer usuário que não tenha o 'is_staff' como 'true'
    
    # IsAuthenticatedOrReadOnly - permitirá que usuários autenticados executem qualquer solicitação.
    # Solicitações para usuários não autenticados somente serão permitidas se o método de solicitação for um dos métodos “seguros”
    
       
    permission_classes = (IsAuthenticated,  )
    
    authentication_classes = (TokenAuthentication, )
    
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
    