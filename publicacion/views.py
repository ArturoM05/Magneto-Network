from django.shortcuts import render
from cuenta.models import Usuario
from .models import Publicacion
from django.contrib import messages

def get_user(request):
    ip_actual = request.META.get('REMOTE_ADDR')
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip_actual = request.META['HTTP_X_FORWARDED_FOR'].split(',')[0]
    # Buscar el usuario con la última IP igual a la IP actual
    return Usuario.objects(ultima_ip=ip_actual).first()

def home_algorithm(request):
    user = get_user(request)
    if request.method == 'POST':
        if 'post_content' in request.POST:
            post_content = request.POST.get('post_content')
            publicacion = Publicacion(user=user.nombre,text=post_content, likes=0)
            publicacion.save()
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

