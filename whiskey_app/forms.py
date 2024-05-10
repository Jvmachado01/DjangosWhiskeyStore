# Do módulo django importa forms, que contém funcionalidade para manipular forms
from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'quantidade']

class ProdutoFormAtualizar(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'quantidade']

    def __init__(self, *args, **kwargs):
        super(ProdutoFormAtualizar, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['placeholder'] = 'Novo nome'
        self.fields['quantidade'].widget.attrs['placeholder'] = 'Nova quantidade'


'''
Essencialmente, estamos criando um formulário (ProdutoForm) que 
está vinculado ao modelo Produto. Ao fazer isso,
o Django pode lidar automaticamente com a validação dos dados inseridos 
no formulário e a criação/atualização dos objetos do modelo correspondentes 
no banco de dados. 
Isso torna o processo de criar e manipular formulários no Django muito mais 
simples e eficiente.
'''        