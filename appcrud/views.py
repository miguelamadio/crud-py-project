from django.shortcuts import render, redirect
from appcrud.forms import LivrosForm
from appcrud.models import Livros
from appcrud.forms import VendedorForm
from appcrud.models import Vendedor

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
    
def view(request, pk): #função de visualização, recebe uma requisição e a chave primária como parâmetro
    data = {} #cria dicionário para armazenar os dados a serem passados para o template
    data['db'] = Livros.objects.get(pk = pk) #pega o valor da chave prim. e armazena no dicionário 
    return render(request, 'view.html', data) #renderiza o view.html com os dados do dicionário


def edit(request, pk): #recebe uma requisição e a chave primária como parâmetro
    data = {} #cria dicionário para armazenar os dados a serem passados para o template
    data['db'] = Livros.objects.get(pk=pk) #pega o valor da chave prim. e armazena no dicionário 
    data['form'] = LivrosForm(instance=data['db']) #recebe dados do formulario chamando uma instancia do DB  
    return render(request, 'form.html', data) #renderiza o form.html com os dados do dicionário

def update(request, pk): #recebe uma requisição e a chave primária como parâmetro
    data = {}  #cria dicionário para armazenar os dados a serem passados para o template
    data['db'] = Livros.objects.get(pk=pk) #Obtém o objeto do banco de dados com a chave primária fornecida
    form = LivrosForm(request.POST or None, instance=data['db']) # instance é usado para preencher o formulário com os dados do objeto do banco de dados  
    #pega os dados que estão vindo via post e fazer o update
    if form.is_valid(): #se o formulário for válido
        form.save() #vai salvar os dados no DB
        return redirect('home') #Redireciona pra home page
    

def delete(request, pk): #recebe uma requisição e a chave primária como parâmetro
    db = Livros.objects.get(pk=pk) #Obtém o objeto do banco de dados com a chave primária fornecida  
    db.delete() #deleta a linha da tabela de acordo com pk atual
    return redirect('home') #Redireciona pra home page

##########################################
                #VENDEDOR
##########################################
def home_vendedor(request):
    data = {} #cria dicionário para armazenar os dados a serem passados para o template
    data['db'] = Vendedor.objects.all() #capta todos os dados da tabela 'Livros'
    return render(request,'index_vendedor.html', data) #Redireciona pra index


def form_vendedor(request):
    data = {} #cria dicionário para armazenar os dados a serem passados para o template
    data['form'] = VendedorForm() #pega os valores pre definidos e exibe no formulario
    return render(request, 'form_vendedor.html', data) #renderiza o form.html com os dados do dicionário

def create_vendedor(request):
    form = VendedorForm(request.POST or None) #recebe os dados lá do form.index por uma requisição POST
    if form.is_valid(): #se o formulário for válido
        form.save() #vai salvar os dados no DB
        return redirect('home_vendedor') #Redireciona pra home page
    
def view_vendedor(request, pk): #função de visualização, recebe uma requisição e a chave primária como parâmetro
    data = {} #cria dicionário para armazenar os dados a serem passados para o template
    data['db'] = Vendedor.objects.get(pk = pk) #pega o valor da chave prim. e armazena no dicionário 
    return render(request, 'view_vendedor.html', data) #renderiza o view.html com os dados do dicionário


def edit_vendedor(request, pk): #recebe uma requisição e a chave primária como parâmetro
    data = {} #cria dicionário para armazenar os dados a serem passados para o template
    data['db'] = Vendedor.objects.get(pk=pk) #pega o valor da chave prim. e armazena no dicionário 
    data['form'] = VendedorForm(instance=data['db']) #recebe dados do formulario chamando uma instancia do DB  
    return render(request, 'form_vendedor.html', data) #renderiza o form.html com os dados do dicionário

def update_vendedor(request, pk): #recebe uma requisição e a chave primária como parâmetro
    data = {}  #cria dicionário para armazenar os dados a serem passados para o template
    data['db'] = Vendedor.objects.get(pk=pk) #Obtém o objeto do banco de dados com a chave primária fornecida
    form = VendedorForm(request.POST or None, instance=data['db']) # instance é usado para preencher o formulário com os dados do objeto do banco de dados  
    #pega os dados que estão vindo via post e fazer o update
    if form.is_valid(): #se o formulário for válido
        form.save() #vai salvar os dados no DB
        return redirect('home_vendedor') #Redireciona pra home page
    

def delete_vendedor(request, pk): #recebe uma requisição e a chave primária como parâmetro
    db = Vendedor.objects.get(pk=pk) #Obtém o objeto do banco de dados com a chave primária fornecida  
    db.delete() #deleta a linha da tabela de acordo com pk atual
    return redirect('home_vendedor') #Redireciona pra home page