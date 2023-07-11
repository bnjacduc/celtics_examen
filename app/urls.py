from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views




urlpatterns = [
    path('lista', views.lista_productos, name='lista_productos'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<str:codigo>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<str:codigo>/', views.eliminar_producto, name='eliminar_producto'),
    path('estadio/', views.estadio, name="estadio"),
    path('base/', views.base, name="base"),
    path('jugadores/', views.jugadores, name="jugadores"),
    path('', views.inicio, name="inicio"),
    path('equipos/', views.equipos, name="equipos"),
    path('entradas/', views.entradas, name="entradas"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('socio/', views.socio, name='socio'),
]

