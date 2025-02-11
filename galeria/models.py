from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Fotografia(models.Model):
  
    #Cria uma lista de tuplas com as categorias já existentes no site para evitar que sejam criadas outras categorias que não devem existir
    OPCOES_CATEGORIA = [
      ("NEBULOSA", "Nebulosa"),
      ("ESTRELA", "Estrela"),
      ("GALÁXIA", "Galáxia"),
      ("PLANETA", "Planeta")
    ]
  
   #inicia o campo nome com o tipo char, limita o numero maximo de caracteres a 100, não permite que seja null e nem blank (x = "")
    nome = models.CharField(max_length = 100, null = False, blank = False)
    legenda = models.CharField(max_length = 150, null = False, blank = False)
    categoria = models.CharField(max_length = 100, choices = OPCOES_CATEGORIA, default = '')
    descricao = models.TextField(null = False, blank = False)
    #caminho da foto
    foto = models.ImageField(upload_to = "fotos/%Y/%m/%d/", blank = True)
    publicada = models.BooleanField(default = False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank = False)
    usuario = models.ForeignKey(
      to = User,
      on_delete = models.SET_NULL,
      null = True,
      blank = False,
      related_name = "user" #forma de localizar qual a tabela
    )
    
    def ___str__(self):
        return self.nome