from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm, ProdutoFormAtualizar

def home(request):
    produtos = Produto.objects.all()
    form_adicionar = ProdutoForm()
    form_atualizar = ProdutoFormAtualizar()

    if request.method == "POST":
        if 'adicionar' in request.POST:
            form_adicionar = ProdutoForm(request.POST)
            if form_adicionar.is_valid():
                form_adicionar.save()
                return redirect("home")
        elif 'atualizar' in request.POST:
            produto_id = request.POST.get('produto_id')
            produto = Produto.objects.get(pk=produto_id)
            form_atualizar = ProdutoFormAtualizar(request.POST, instance=produto)
            if form_atualizar.is_valid():
                form_atualizar.save()
                return redirect("home")
        elif 'excluir' in request.POST:  # Nova lógica para exclusão de produto
            produto_id = request.POST.get('produto_id')
            produto = Produto.objects.get(pk=produto_id)
            produto.delete()
            return redirect("home")

    context = {
        "form_adicionar": form_adicionar,
        "form_atualizar": form_atualizar,
        "produtos": produtos
    }

    return render(request, 'home.html', context)
