from django.shortcuts import render
from django.http import JsonResponse
from .models import AreaInteres
from cuenta.models import Usuario

def add_area_interes(request):
    """    usuario_id = Usuario.request.session.get('usuario_id') 
        usuario = Usuario.objects(id=usuario_id).first()
        if request.method == 'POST':
            if "area_interes_list" in request.POST:
                areas_interes_id = list(request.POST.get("area_interes_list"))
                for area_id in areas_interes_id:
                    area_interes = AreaInteres.objects(id=area_id).first()
                    usuario.areas_interes.append(area_interes)
                usuario.save()
    """
    pass

def delete_area_interes(request):
    pass


def show_area_interes(request):
    usuario_id = request.session.get('usuario_id')
    usuario = Usuario.objects(id=usuario_id).first()
    areas_interes = [{'id': '3t123131','nombre': 'Deporte'},  {'id': '9123t213dfgf','nombre': 'Cocina'},{'id': '3fsd323131','nombre': 'Deporte'},  {'id': '9123t213eqwfgf','nombre': 'Cocina'},  {'id': '3t1','nombre': 'Deporte'},  {'id': '912dfgf','nombre': 'Cocina'}, {'id': '1','nombre': 'Deporte'},  {'id': '2f','nombre': 'Cocina'}]
    
    if usuario:
        areas_interes.extend(usuario.areas_interes)
    
    areas_populares = AreaInteres.objects(popularity__gt=60)
    areas_interes.extend(areas_populares)
    # areas_interes_serializadas = [{'id': str(area.id), 'nombre': area.nombre} for area in areas_interes]
    areas_interes_serializadas = areas_interes
    return JsonResponse({'areas_interes': areas_interes_serializadas})