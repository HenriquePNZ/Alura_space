from datetime import datetime
from django.db import models

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
    foto = models.CharField(max_length = 100, null = False, blank = False)
    publicada = models.BooleanField(default = False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank = False)
    
    def ___str__(self):
        return f"Fotografia [nome= {self.nome} ]"