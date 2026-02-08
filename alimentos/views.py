from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Alimento, Compra, Receta
from .forms import AlimentoForm, CompraForm, RecetaForm


# =====================
# AUTH
# =====================

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("lista_alimentos")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "alimentos/login.html")


def registro(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, "Cuenta creada correctamente")
            return redirect("login")

    return render(request, "alimentos/registro.html")


def logout_view(request):
    logout(request)
    return redirect("login")


# =====================
# ALIMENTOS
# =====================

@login_required
def lista_alimentos(request):
    alimentos = Alimento.objects.filter(usuario=request.user)
    return render(request, "alimentos/lista_alimentos.html", {
        "alimentos": alimentos
    })


@login_required
def agregar_alimento(request):
    if request.method == "POST":
        form = AlimentoForm(request.POST, request.FILES)
        if form.is_valid():
            alimento = form.save(commit=False)
            alimento.usuario = request.user
            alimento.save()
            return redirect("lista_alimentos")
    else:
        form = AlimentoForm()

    return render(request, "alimentos/agregar.html", {
        "form": form
    })


# =====================
# COMPRAS
# =====================

@login_required
def lista_compras(request):
    compras = Compra.objects.filter(usuario=request.user)
    return render(request, "alimentos/compras.html", {
        "compras": compras
    })


@login_required
def agregar_compra(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.usuario = request.user
            compra.save()
            return redirect("lista_compras")
    else:
        form = CompraForm()

    return render(request, "alimentos/agregar_compra.html", {
        "form": form
    })


@login_required
def marcar_comprado(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id, usuario=request.user)
    compra.comprado = True
    compra.save()
    return redirect("lista_compras")


# =====================
# RECETAS (PÚBLICAS)
# =====================

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, "alimentos/recetas.html", {
        "recetas": recetas
    })


@login_required
def agregar_receta(request):
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.usuario = request.user
            receta.save()
            return redirect("lista_recetas")
    else:
        form = RecetaForm()

    return render(request, "alimentos/agregar_receta.html", {
        "form": form
    })


def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    return render(request, "alimentos/detalle_receta.html", {
        "receta": receta
    })


@login_required
def lista_inventario(request):
    alimentos = Alimento.objects.all()
    return render(request, "alimentos/lista_alimentos.html", {
        "alimentos": alimentos
    })


@login_required
def eliminar_alimento(request, id):
    alimento = get_object_or_404(Alimento, id=id)
    alimento.delete()
    return redirect("lista_inventario")


@login_required
def eliminar_compra(request, id):
    compra = get_object_or_404(Compra, id=id, usuario=request.user)
    compra.delete()
    return redirect('lista_compras')

@login_required
def eliminar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    receta.delete()
    return redirect('lista_recetas')
