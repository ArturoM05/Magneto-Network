from django.shortcuts import render
from cuenta.models import Usuario
from .models import Publicacion
from django.contrib import messages


def home_algorithm(request):
    usuario_id = request.session.get('usuario_id')
    user = Usuario.objects(id=usuario_id).first()
    if request.method == 'POST':
        if 'post_content' in request.POST:
            post_content = request.POST.get('post_content')
            publicacion = Publicacion(user=user.nombre,text=post_content, likes=0)
            publicacion.save()
            messages.info(request, 'tu post se ha publicado')
        if 'like_post' in request.POST:
            post_id = request.POST.get('like_post')
            publicacion = Publicacion.objects(id=post_id).first()
            publicacion.likes += 1
            publicacion.save()
    publicaciones = list(Publicacion.objects())
    if user:
        print(user.nombre)
        return render(request, 'home1.html', {'usuario': user, 'publicaciones': publicaciones})
    else:
        messages.error(request, 'tienes que iniciar sesion primero')
        return render(request, 'login.html')

