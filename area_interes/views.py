from django.shortcuts import redirect
from django.http import JsonResponse
from .models import AreaInteres
from cuenta.models import Usuario

def add_area_interes(request):
    if request.method == 'POST':
        nombre_area = request.POST.get('nombre_area', None)
        if nombre_area:
            usuarios = Usuario.objects.count()
            popularity = (1/(usuarios+1))*100

            area = AreaInteres(nombre=nombre_area,interested=1,popularity=popularity)
            area.save()   
            return redirect('/area_interes/show')
        else:
            return JsonResponse({'success': False, 'message': 'No se recibió el nombre del área de interés'})
    return JsonResponse({'success': False, 'message': 'Método no permitido'})

def delete_area_interes(request):
    pass


def show_area_interes(request):
    areas_interes = []
    usuario_id = request.session.get('usuario_id')
    user = Usuario.objects(id=usuario_id).first()        
    areas_populares = AreaInteres.objects(popularity__gt=0)
    if user:
        for area in areas_populares:
            if not area in user.areas_interes:
                areas_interes.append(area)
    else:
        areas_interes.extend(areas_populares)     
    areas_interes_serializadas = [{'id': str(area.id), 'nombre': area.nombre} for area in areas_interes]
    return JsonResponse({'areas_interes': areas_interes_serializadas})