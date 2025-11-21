from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm


# ============================================
# LOGIN
# ============================================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            # 🔥 Redirección corregida con namespace
            return redirect("plataforma:lista_proyectos")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "accounts/login.html")


# ============================================
# LOGOUT
# ============================================
def logout_view(request):
    logout(request)
    return redirect("accounts:login")   # ← namespace correcto


# ============================================
# REGISTER
# ============================================
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada con éxito. Ahora inicia sesión.")
            return redirect("accounts:login")   # ← usar el namespace siempre
        else:
            messages.error(request, "Corrige los errores del formulario.")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})
