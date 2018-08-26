from django.db import models

# Create your models here.

class Empresa(models.Model):#define o form aqui
	#chaves estrangeiras????
	razaoSocial = models.CharField(max_length=255)
	cnpj = models.CharField(max_length=255)
	email = models.CharField(max_length=255, null=True)
	password = models.CharField(max_length=255, null=True)
	transportadora = models.CharField(max_length=255, null=True)
	keyWords = models.CharField(max_length=255)
	processoInterno = models.IntegerField(null=True);
	processoExterno = models.IntegerField(null=True);
	transportadora = models.CharField(max_length=255);

	class Meta:
		db_table = 'empresas' # nome para o banco
		verbose_name = 'empresa' 
		verbose_name_plural = 'empresas'