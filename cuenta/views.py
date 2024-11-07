from django.shortcuts import render, redirect
from .models import Usuario
from area_interes.models import AreaInteres
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime

def registrar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        pn = request.POST.get('phone_number')
        bd = request.POST.get('birthdate')
        if bd:
            birthdate = datetime.strptime(bd, '%Y-%m-%d').date()
        description = request.POST.get('description')
        password = request.POST.get('password')
        
        if Usuario.objects(email=email):
            messages.error(request, 'El email ya está registrado.')
        else:     
            hashed_password = make_password(password)
            usuario = Usuario(nombre=nombre, email=email, password=hashed_password, birthdate=birthdate, phone_number=pn, description=description)
            usuario.save()
            areas_interes_id = request.POST.get('areas_seleccionadas').split(",")
            for area_id in areas_interes_id:
                area = AreaInteres.objects(id=area_id).first()
                area.interested += 1
                area.update_popularity()
                usuario.areas_interes.append(area)
                area.save()
            usuario.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('login')

    return render(request, 'registro.html')

def login_usuario(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            usuario = Usuario.objects.get(email=email)
            # Verificar la contraseña
            if check_password(password, usuario.password):
                messages.success(request, 'Inicio de sesión exitoso.')
                request.session['usuario_id'] = str(usuario.id)
                return redirect('home1')
            else:
                print('Contraseña incorrecta.')
                messages.error(request, 'Contraseña incorrecta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'El usuario no existe.')

    return render(request, 'login.html')

def logout_usuario(request):
    logout(request)
    return redirect('login')

        