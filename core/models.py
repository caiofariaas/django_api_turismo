from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacoes
from endereco.models import Endereco

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    desc = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacoes)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos-turisticos', null=True, blank=True)
    
    # Podemos usar o '@property' ao invés do SerializerMethodField
    
    @property
    def descricao_completa2(self):
        return '%s - %s' % (self.nome, self.desc)
    
    def __str__(self):
        return self.nome
