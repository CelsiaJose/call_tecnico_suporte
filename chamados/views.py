from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import formChamados
from .formseditar import formChamadoseditar
from django.contrib import messages
from .models import Chamados
#Imports para o viewSet
from .serializers import UserSerializer,ChamadoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
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

    def perform_create(self, serializer):
        # Quando criar um chamado pela API, usa o usuário logado como "usuario"
        serializer.save(usuario=self.request.user) #Ou seja: não precisa o cliente enviar o usuário no JSON — o backend define sozinho.O usuario logado,ou seja salva os dados em serialzers e também o usuario que fez a requisicao


