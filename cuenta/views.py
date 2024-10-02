from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages
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
            usuario = Usuario(nombre=nombre, email=email, password=hashed_password, birthdate=birthdate, phone_number=pn, description=description, sesion = 'Activate')
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
                # Autenticación exitosa
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('home')
            else:
                messages.error(request, 'Contraseña incorrecta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'El usuario no existe.')

    return render(request, 'login.html')


def home_algorithm(request):
    return render(request, 'home.html')
