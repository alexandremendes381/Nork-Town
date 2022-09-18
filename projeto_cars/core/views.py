from ast import And, Return
from django.shortcuts import render, redirect
from .forms import ClienteForm
from .forms import LocacaoForm
from .models import Cliente, Locacao
from django.http import JsonResponse

def index(request):
    return render(request, 'core/index.html')

def clientes(request):
    data = {}
    data['clientes'] = Cliente.objects.all()  # Carregando clientes do banco

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Salva
            return redirect('url_cliente')
    else:
        data['form'] = ClienteForm()
        #form = ClienteForm()
    return render(request, 'core/clientes.html', data)

def locacoes(request):
    data = {}
    data['locacoes'] = Locacao.objects.all()  # Carrega clientes do banco

    if request.method == 'POST':
        #print(request.POST)
        id_cliente= request.POST.get('cliente')
        tipo_cliente = request.POST.get('tipo')
        # cor_cliente = request.POST.get('cor')
        # print(id_cliente)
        # print(tipo_cliente)
        # print(cor_cliente)
        x = Cliente.objects.filter(pk=id_cliente).first().locacao_set.all()
        for i in x: 
            if i.tipo == tipo_cliente: # faz a comparacao do banco de dados com o cliente e carro e autoriza ou nao o prosseguimento.
                return JsonResponse({'ERROR':'CLIENTE JA COM VEICULO CADASTRADO, POR FAVOR REFAZER OPERACAO COM VEICULO DIFERENTE. CASO O CLIENTE JA TENHA OS TRES VEICULOS REGISTRADOS E IMPOSSIVEL REALIZAR A OPERACAOO.'}) 
        form = LocacaoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva as informacoes
            return redirect('url_locacao')
    else:
        data['form'] = LocacaoForm()
        form = ClienteForm()
    return render(request, 'core/locacoes.html', data)


# ATUALIZA

def atualiza_cliente(request, pk):
    data = {}
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente) #Passar o formulario preenchido

    # Verificar se o form é valido
    if form.is_valid():
        form.save()  # Salva
        return redirect('url_cliente')  # redireciona para a listagem

    data['form'] = form
    data['clientes'] = cliente # Envia a transação pela URL para remover

    return render(request, 'core/atualizacliente.html', data)

def atualiza_locacao(request, pk):
    data = {}
    locacao = Locacao.objects.get(pk=pk)
    form = LocacaoForm(request.POST or None, instance=locacao)

    if form.is_valid():
        form.save()
        return redirect('url_locacao')

    data['form'] = form

    return render(request, 'core/atualizalocacao.html', data)

# REMOVER

def remover_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('url_cliente')

def remover_locacao(request, pk):
    locacao = Locacao.objects.get(pk=pk)
    locacao.delete()
    return redirect('url_locacao')


