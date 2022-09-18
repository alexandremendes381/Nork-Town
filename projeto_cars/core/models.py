from django.db import models

# Create your models here.


class Cliente(models.Model):
    ATIVO = 'ATIVO'
    INATIVO = 'INATIVO'
    STATUS = (
        (ATIVO, 'Ativo'),
        (INATIVO, 'Inativo'),
    )

    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15, unique=True) #define um cpf unico para impossibilidade de pessoas duplicadas
    status = models.CharField(max_length=10, choices=STATUS)


    def __str__(self):
        return self.nome


class Locacao(models.Model):

    
    HATCH = 'HATCH'
    SEDAN = 'SEDAN'
    CONVERSIVEL = 'CONVERSIVEL'
        
    TIPO = (
        (HATCH, 'Hatch'),
        (SEDAN, 'Sedan'),
        (CONVERSIVEL, 'Conversivel') 
            
        )  
    
    AMARELO = 'AMARELO'
    AZUL = 'AZUL'
    CINZA = 'CINZA'
    
    COR = (
        (AMARELO, 'Amarelo'),  
        (AZUL, 'Azul'),
        (CINZA, 'Cinza')
    )
        
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=15, choices=TIPO)
    cor = models.CharField(max_length=15, choices=COR)
    class Meta:
        verbose_name_plural = 'Locações'


