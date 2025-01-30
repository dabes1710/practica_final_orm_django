from django.shortcuts import render, get_object_or_404, redirect
from .models import Laboratorio
from .forms import LaboratorioForm 

# Mostrar lista de laboratorios
def listar_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio/listar.html', {'laboratorios': laboratorios})

# Crear un nuevo laboratorio
def crear_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_laboratorios')
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorio/formulario.html', {'form': form})

# Editar un laboratorio existente
def editar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('listar_laboratorios')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorio/formulario.html', {'form': form})

# Eliminar un laboratorio
def eliminar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('listar_laboratorios')
    return render(request, 'laboratorio/confirmar_eliminar.html', {'laboratorio': laboratorio})


