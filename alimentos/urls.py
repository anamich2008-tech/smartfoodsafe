from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("registro/", views.registro, name="registro"),
    path("logout/", views.logout_view, name="logout"),

    path("", views.lista_alimentos, name="lista_alimentos"),

    path("alimentos/agregar/", views.agregar_alimento, name="agregar_alimento"),

    path("compras/", views.lista_compras, name="lista_compras"),
    path("compras/agregar/", views.agregar_compra, name="agregar_compra"),
    path("compras/marcar/<int:compra_id>/", views.marcar_comprado, name="marcar_comprado"),

    path("recetas/", views.lista_recetas, name="lista_recetas"),
    path("recetas/agregar/", views.agregar_receta, name="agregar_receta"),
    path("recetas/<int:receta_id>/", views.detalle_receta, name="detalle_receta"),

    path("inventario/", views.lista_inventario, name="lista_inventario"),
    path("eliminar/<int:id>/", views.eliminar_alimento, name="eliminar_alimento"),

    path('compras/eliminar/<int:id>/', views.eliminar_compra, name='eliminar_compra'),
    path('recetas/eliminar/<int:id>/', views.eliminar_receta, name='eliminar_receta'),



]

