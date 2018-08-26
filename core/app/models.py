from django.db import models

# Create your models here.

class Empresa(models.Model):#define o form aqui
	#chaves estrangeiras????
	razaoSocial = models.CharField(max_length=255)
	cnpj = models.CharField(max_length=255)
	keyWords = models.CharField(max_length=255)
	processoInterno = models.IntegerField();
	processoExterno = models.IntegerField();
	transportadora = models.CharField(max_length=255);

	class Meta:
		db_table = 'itens' # nome para o banco
		verbose_name = 'item' 
		verbose_name_plural = 'itens'