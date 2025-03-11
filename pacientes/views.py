from django.shortcuts import render,HttpResponse,redirect
from .models import Pacientes
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
    return HttpResponse(id)