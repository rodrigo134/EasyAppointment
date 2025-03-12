from django.shortcuts import render,HttpResponse,redirect
from .models import Pacientes, Tarefas, Consultas
from django.contrib import messages
from django.contrib.messages import constants



# Create your views here.

def pacientes(request):
    if request.method == 'GET':
        pacientes = Pacientes.objects.all()
        return render(request , 'pacientes.html',{'queixas': Pacientes.queixa_choices,'pacientes': pacientes}) #inclusão de queixas que é uma tupla de tuplas do sintoma
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        queixa = request.POST.get('queixa')
        foto = request.FILES.get('foto')
        paciente = Pacientes(
             nome=nome,
             email=email,
             telefone=telefone,
             queixa=queixa,
             foto=foto)  #valor atributo=oque quero salvar
        if len(nome.strip()) == 0 or not foto:
            messages.add_message(request,constants.ERROR, "cadastro nao realizado")# request,type message , text
            return redirect('pacientes')
        
        
        messages.add_message(request,constants.SUCCESS, "cadastro  realizado")# request,type message , text
        paciente.save()
         
         
         
    return redirect('pacientes') #atributo name em url.py


def pacientes_view(request,id):
    paciente = Pacientes.objects.get(id =id)
    if request.method == 'GET':
        tarefas = Tarefas.objects.all()
        consultas = Consultas.objects.filter(paciente=paciente)
        return render(request, 'paciente.html', {'paciente':paciente, 'tarefas':tarefas,'consultas': consultas})
    elif request.method == 'POST':
        humor = request.POST.get('humor')
        registro_geral = request.POST.get('registro_geral')
        video = request.FILES.get('video')
        tarefas = request.POST.getlist('tarefas')
        consultas = Consultas(
            humor= int(humor),
            registro_geral= registro_geral,
            video=video,
            paciente = paciente
        )
        consultas.save()
        #primeiro salva a consulta pra depois adicionar consulta
        
        for i in tarefas:
            tarefa = Tarefas.objects.get(id=i)
            consultas.tarefas.add(tarefa)
        consultas.save()
        messages.add_message(request,constants.SUCCESS, 'Consulta Registrada com Sucesso!')
    return redirect(f'/pacientes/{id}')


def atualizar_paciente(request,id):
    pagamento = request.POST.get('pagamento')
    paciente = Pacientes.objects.get(id=id)
    
    status = True if pagamento =='ativo' else False
    paciente.pagamento = status
    paciente.save()
    
    return redirect(f'/pacientes/{id}')

def excluir_consulta(request, id):
    consulta = Consultas.objects.get(id=id)
    consulta.delete()
    return redirect(f'/pacientes/{consulta.paciente.id}')