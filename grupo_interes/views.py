from django.shortcuts import render
from cuenta.models import Usuario
from publicacion.models import Publicacion
from .models import GrupoInteres
from django.shortcuts import render, redirect
from .models import Usuario
from area_interes.models import AreaInteres
from datetime import datetime
# exxplore grupo interes

def show_new_grupo_interes(request):
    return render(request, 'explore_groups.html', {'message': 'Por hacer'})

def create_grupo_interes(request):
    usuario_id = request.session.get('usuario_id')
    user = Usuario.objects(id=usuario_id).first()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        description = request.POST.get('description')    
        if GrupoInteres.objects(nombre=nombre):
            pass
        else:     
            grupo = GrupoInteres(nombre=nombre, description=description)
            grupo.members.append(user)
            grupo.update_popularity()
            grupo.save()
            areas_interes_id = request.POST.get('areas_seleccionadas').split(",")
            for area_id in areas_interes_id:
                area = AreaInteres.objects(id=area_id).first()
                area.interested += 1
                area.update_popularity()
                grupo.areas_interes.append(area)
                area.save()
            grupo.save()
            return redirect('feed')
    return render(request, 'create_group.html')

def join_grupo_interes(request):
    pass

#  view current user grupos de interess

def grupo_interes_feed(request):
    usuario_id = request.session.get('usuario_id')
    user = Usuario.objects(id=usuario_id).first()
    if request.method == 'POST':
        if 'post_content' in request.POST and 'grupo_seleccionado' in  request.POST:
            post_content = request.POST.get('post_content')
            grupo = request.POST.get('grupo_seleccionado')
            publicacion = Publicacion(user=user,text=post_content, likes=0, group=grupo)
            publicacion.save()
    user_groups = GrupoInteres.objects(members=user)
    publicaciones = list(Publicacion.objects(group__in=user_groups))
    if user:
        return render(request, 'feed_groups.html', {'usuario': user, 'publicaciones': publicaciones,'grupos': user_groups })
    else:
        return render(request, 'login.html')

def grupo_interes_profile(request, id):
    grupo = GrupoInteres.objects(id=id).first()
    publicaciones = list(Publicacion.objects(group=grupo))
    return render (request, 'group_profile.html',{'user': grupo, 'posts': publicaciones})