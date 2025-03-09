from django.shortcuts import render,HttpResponse,redirect
from .models import Pacientes




# Create your views here.
def pacientes(request):
    if request.method == 'GET':
        return render(request , 'pacientes.html',{'queixas': Pacientes.queixa_choices})
    else:
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
         
         paciente.save()
         
         
         
         return redirect('pacientes')


