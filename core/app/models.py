from django.db import models

# Create your models here.

class Empresa(models.Model):#define o form aqui
	#chaves estrangeiras????
	razao_social = models.CharField(max_length=255)
	nome_fantasia = models.CharField(max_length=255)
	cnpj = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	filtro = models.CharField(max_length=255)
	proceso_interno = models.IntegerField();
	processo_externo = models.IntegerField();
	transportadora = models.CharField(max_length=255);

	'''carater = models.IntegerField()
	quantidade = models.IntegerField()
	imagem = models.FileField(upload_to='imagens/', null=False)
	status = models.ForeignKey(StatusItem, on_delete=models.CASCADE)
	tipoItem = models.ForeignKey(TipoItem, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	'''
	class Meta:
		db_table = 'itens' # nome para o banco
		verbose_name = 'item' 
		verbose_name_plural = 'itens'