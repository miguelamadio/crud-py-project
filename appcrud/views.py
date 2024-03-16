from django.shortcuts import render, redirect
from appcrud.forms import LivrosForm
from appcrud.models import Livros

# Create your views here.

def home(request):
    data = {} #cria dicionário para armazenar os dados a serem passados para o template
    data['db'] = Livros.objects.all() #capta todos os dados da tabela 'Livros'
    return render(request,'index.html', data) #Redireciona pra index


def form(request):
    data = {} #cria dicionário para armazenar os dados a serem passados para o template
    data['form'] = LivrosForm() #pega os valores pre definidos e exibe no formulario
    return render(request, 'form.html', data) #renderiza o form.html com os dados do dicionário

def create(request):
    form = LivrosForm(request.POST or None) #recebe os dados lá do form.index por uma requisição POST
    if form.is_valid(): #se o formulário for válido
        form.save() #vai salvar os dados no DB
        return redirect('home') #Redireciona pra home page
    
def view(request, pk): #Define a função de visualização, que recebe a chave primária como parâmetro
    data = {} #cria dicionário para armazenar os dados a serem passados para o template
    data['db'] = Livros.objects.get(pk = pk) #pega o valor da chave prim. e armazena no dicionário 
    return render(request, 'view.html', data) #renderiza o view.html com os dados do dicionário

