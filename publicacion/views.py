import  json
from django.shortcuts import render
from cuenta.models import Usuario
from .models import Publicacion
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home_algorithm(request):
    usuario_id = request.session.get('usuario_id')
    user = Usuario.objects(id=usuario_id).first()
    if request.method == 'POST':
        if 'post_content' in request.POST:
            post_content = request.POST.get('post_content')
            publicacion = Publicacion(user=user,text=post_content, likes=0)
            publicacion.save()
            messages.info(request, 'tu post se ha publicado')
    publicaciones = list(Publicacion.objects())
    if user:
        return render(request, 'home1.html', {'usuario': user, 'publicaciones': publicaciones})
    else:
        messages.error(request, 'tienes que iniciar sesion primero')
        return render(request, 'login.html')


@csrf_exempt  # Considera la seguridad en tu implementación
def like_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data.get('post_id')

        # Lógica para dar like a la publicación
        publicacion = Publicacion.objects(id=post_id).first()
        publicacion.likes += 1
        publicacion.save()

        return JsonResponse({'success': True, 'likes': publicacion.likes})

    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

def user_profile(request, id):
    user = Usuario.objects(id=id).first()
    publicaciones = list(Publicacion.objects(user=user))
    return render(request, 'profile.html',{'user': user, 'posts': publicaciones})