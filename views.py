from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm

def cadastro_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/cadastro.html', {'form': form})

def listagem_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/listagem.html', {'pacientes': pacientes})

def index(request):
    return render(request, 'pacientes/index.html')

def atualizar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('listagem_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/atualizar.html', {'form': form, 'paciente': paciente})
    
def excluir_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('listagem_pacientes')
    return render(request, 'pacientes/excluir.html', {'paciente': paciente})
