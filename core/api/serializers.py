from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecosSerializer
from avaliacoes.api.serializers import AvaliacoesSerializer
from comentarios.api.serializers import ComentariosSerializer

class PontoTuristicoSerializer(ModelSerializer):
    
    # NestedRelationships
    # Utilizando o Serializer das outras classes para poder visualizar seus itens
    # em Pontos turisticos, ao contrario disso ele mostra apenas o ID 
    
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecosSerializer(many=False)
    avaliacoes = AvaliacoesSerializer(many=True)
    comentarios = ComentariosSerializer(many=True)

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'desc', 'aprovado', 'atracoes',
            'comentarios', 'avaliacoes', 'endereco', 'foto'
            )
        
        
    