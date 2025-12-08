from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate



from django.contrib.auth.models import User
from .forms import formChamados
from .formseditar import formChamadoseditar
from .formcadastro import formCadastro
from django.contrib import messages
from .models import Chamados,Perfil
from django.utils import timezone
#Imports para o viewSet
from .serializers import UserSerializer,ChamadoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

@login_required
def chamado_listar(request):

    chamados = Chamados.objects.all()
    return render (request, 'chamados/chamado_listar.html',{'chamados':chamados})


@login_required
def chamados_Criar(request):

    if request.method=="POST":
         form=formChamados(request.POST) # este quest.post signifca com os dados preenchidos. 
         if form.is_valid():
            chamado=form.save(commit=False) # ajuda a ajustar um campo neste caso o campo user que ja esta ao formulario 
            chamado.usuario = request.user # é o usuario actual logado sendo gravado por isso o commit false na variavel
            chamado.save()
            return redirect('chamado_listar' )
            messages.success(request, "Chamado criado com sucesso.")
         else:
            print("Preencha devidamente")#Mostra os erros 
    else:
        form=formChamados()
        
    return render(request ,'chamados/chamado_criar.html',{'form':form})

def chamado_lista_detal(request,id):
    chamado_detal=get_object_or_404(Chamados , id=id)

    return render(request,'chamados/chamado_lista_detal.html',{'chamado_detal':chamado_detal})

def chamado_editar(request,id):
    chamado_editar=get_object_or_404(Chamados,id=id)
    if request.method=="POST":
        form=formChamadoseditar(request.POST,instance=chamado_editar) # este quest.post signifca com os dados preenchidos. 
        if form.is_valid():
            form.save()
            messages.success(request, "Chamado sofreu alteraçoes")
           
            return redirect('chamado_lista_detal' , id=chamado_editar.id)
            
        else:
            print("Preencha devidamente")#Mostra os erros
            print(form.errors) 
    else:
        form=formChamadoseditar(instance=chamado_editar)
        
    return render(request,'chamados/chamado_editar.html',{'form':form})

def chamado_deletar(request,id):
    chamado_rm=get_object_or_404(Chamados,id=id)

    if request.method=="POST":
        chamado_rm.delete()
        return redirect('chamado_listar') 

    #return render(request, 'chamados/chamado_confirm_delete.html', {'chamado': chamado})


# Views do ViewSet

class chamadoViewset(viewsets.ModelViewSet):
    queryset=Chamados.objects.all() # chama tudo do model chamado
    serializer_class=ChamadoSerializer #chama tudo do serializer transforma os dados do chamado em json
    permission_classes = [IsAuthenticated] # Para permitir so usuario autenticado digual @decorate?log
    def get_queryset(self):
         # Primeiro eu vou filtrarr por dados de onde ? Claro que de chamados então vai ou seja aonde pegalos
        qs = Chamados.objects.all()

        #Mas agora já chemei o chamados e o que que tu quer filtrar?
        # Ja sabe aonde pegar status e prioridade? 
        # Sim na minha url e vou guardar o status e prioridade em duas variavies 
        status = self.request.query_params.get('status')# Escrevi no query_params Aberto= Aberto
        prioridade = self.request.query_params.get('prioridade') # Agora no outro = Baixa 
        #Eles gravam estes dois dados da requisicao e apos guardar o que ele faz ?
        #Procura estes dados no qs ,como?
        actualizados_hoje=self.request.query_params.get('hoje')
         
        if actualizados_hoje == '1': # ex: /api/chamados/?hoje=1
            hoje=timezone.now().date()
            qs = qs.filter(atualizado_em__date=hoje) # so o date é so para filtrar a data e nao a hora se nao nao abre nada
       

        if status:
            qs = qs.filter(status=status)
        
        # se entrou por exemplo aberto ele faz o seguinte 
        # vou pegar a minha qs aonde tem todos os dados e la 
        # graças ao filter vou procurar por status no qs que seja igual a Aberto 
        #entao o qs agora é = status Aberto
        # Ou seja mostra só status aberto do qs 
         # Se vier ?prioridade=ALTA, filtra por prioridade
        if prioridade:
            qs = qs.filter(prioridade=prioridade)
        
        #ou seja encontra em qs os dois que quero ele vai me retornar

        return qs


    def perform_create(self, serializer):
        # Quando criar um chamado pela API, usa o usuário logado como "usuario"
        serializer.save(usuario=self.request.user) #Ou seja: não precisa o cliente enviar o usuário no JSON — o backend define sozinho.O usuario logado,ou seja salva os dados em serialzers e também o usuario que fez a requisicao

    # Fazendo Filtragens para aapp


def cadastroUser(request):
    if request.method == 'POST':
        form = formCadastro(request.POST)# este campo ja grava username= xx
                                                               #email igual a x e os outros
        if form.is_valid():# Já avalia ate a palavra pass
            user = form.save()
            Perfil.objects.create(user=user)
            login(request, user)
            return redirect("chamado_listar")
        else:
            return render(request, "chamados/cadastroform.html", {"form": form})

    else:
        form = formCadastro()

    return render(request, "chamados/cadastroform.html", {'form': form})

''' if request.method=='POST':

        username=request.POST["username"]
        print(request.POST)
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1 != password2:

            return render(request, "chamados/cadastroform.html", {"error": "Senhas não coincidem."})
        if User.objects.filter(email=email).exists():# Se lá nos usarios ja tiver este email entao diser nao entre e vai logar
            return render(request, "chamados/cadastroform.html", {"error": "Usuário já existe."})

        user=User.objects.create_user(username=username,email=email,password=password1)
        Perfil.objects.create(user=user) #este usuario no modelo perfil vai se guardado no campo user
        login(request, user)
        return redirect("chamado_listar")
    else:
       form=formCadastro()

    return render(request, 'chamados/cadastroform.html',{'form':form})'''

  

def userlogout(request):
    form = formCadastro(request.POST)
    logout(request) # entra um request e ele sai deste request 
    return render(request, "chamados/cadastroform.html", {'form': form})

def userlogin(request):
   
    if request.method=="POST":
        
        form = formCadastro(request.POST)

        username=request.POST.get('username')
        password1=request.POST.get('password')
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect("chamado_listar")
        else:
            return render(request, "chamados/cadastro_login.html", {
                "error": "Usuário ou senha incorretos.",'form':form })
                      
    else:
        form = formCadastro()

    return render(request, "chamados/cadastro_login.html",{'form': form})


