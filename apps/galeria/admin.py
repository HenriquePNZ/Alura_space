from django.contrib import admin
from apps.galeria.models import Fotografia

# Register your models here.

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome") #Permite que eu clique também no campo nome para acessar os dados do objeto (na plataforma do admin)
    search_fields = ("nome",) # Adiciona um campo de busca na plataforma do admin para que eu consiga encontrar objetos com maior facilidade
    list_filter= ("categoria", "usuario",)
    list_editable = ("publicada",)
    list_per_page = 10 #Limita o numero de objetos a 10 por página
admin.site.register(Fotografia, ListandoFotografias)