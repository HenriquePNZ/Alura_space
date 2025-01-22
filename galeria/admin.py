from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")
    list_display_links = ("id", "nome") #Permite que eu clique também no campo nome para acessar os dados do objeto (na plataforma do admin)
    search_fields = ("nome",) # Adiciona um campo de busca na plataforma do admin para que eu consiga encontrar objetos com maior facilidade
admin.site.register(Fotografia, ListandoFotografias)