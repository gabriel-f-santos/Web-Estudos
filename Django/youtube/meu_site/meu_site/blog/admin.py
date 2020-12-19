from django.contrib import admin
#importa os campos de Post para painel adm
from .models import Post
#Registra Post no painel adm
@admin.register(Post)
# Personaliando o painel adm
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicado', 'status')
    #adiciona busca de artigos
    search_fields = ('titulo','conteudo')
    #preenche slug automático
    prepopulated_fields = {'slug':['titulo'],}
    #adiciona filtros laterais
    list_filter = ('autor','publicado','status')
    #insere guia de ano/mês de publicação
    date_hierarchy = 'publicado'
    #ID de autores - necessário?
    raw_id_fields = ('autor',)



'''
titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    publicado = models.DateTimeField(default=timezone.now())
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 10,
                              choices = STATUS,
                              default = 'rascunho')
'''