from django import forms
 
from .models import Empresa
 
class EmpresaForm(forms.ModelForm):
<<<<<<< HEAD
 
    class Meta:
        model = Empresa
        fields = ['razao_social', 'nome_fantasia', 'cnpj', 'filtro']
=======

	class Meta:
		model = Empresa
		fields = ('razaoSocial','cnpj','keyWords', 'processoInterno', 'processoExterno', 'transportadora')
>>>>>>> 231c1892d79de864c8c6ade7b628748c451156d8
