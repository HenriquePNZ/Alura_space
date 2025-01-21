from django.db import models

class Fotografia(models.Model):
  
   #inicia o campo nome com o tipo char, limita o numero maximo de caracteres a 100, não permite que seja null e nem blank (x = "")
    nome = models.CharField(max_length = 100, null = False, blank = False)
    legenda = models.CharField(max_length = 150, null = False, blank = False)
    descricao = models.TextField(null = False, blank = False)
    #caminho da foto
    foto = models.CharField(max_length = 100, null = False, blank = False)
    
    def ___str__(self):
        return f"Fotografia [nome= {self.nome} ]"