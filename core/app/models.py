from django.db import models

# Create your models here.

class Empresa(models.Model):#define o form aqui
	#chaves estrangeiras????
	razao_social = models.CharField(max_length=255)
	nome_fantasia = models.CharField(max_length=255)
	cnpj = models.CharField(max_length=255)
	email = models.CharField(max_length=255, null=True)
	password = models.CharField(max_length=255, null=True)
	filtro = models.CharField(max_length=255)
	proceso_interno = models.IntegerField(null=True)
	processo_externo = models.IntegerField(null=True)
	transportadora = models.CharField(max_length=255, null=True)

	'''carater = models.IntegerField()
	quantidade = models.IntegerField()
	imagem = models.FileField(upload_to='imagens/', null=False)
	status = models.ForeignKey(StatusItem, on_delete=models.CASCADE)
	tipoItem = models.ForeignKey(TipoItem, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	'''
	class Meta:
		db_table = 'empresas' # nome para o banco
		verbose_name = 'empresa' 
		verbose_name_plural = 'empresas'