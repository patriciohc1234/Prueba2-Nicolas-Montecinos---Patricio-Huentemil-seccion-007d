from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('catalogo/', views.CatalogoListView.as_view(), name='catalogo'),
    path('catalogo/<int:pk>', views.CatalogoDetailView.as_view(), name='catalogo-detail'),
    path('crear/',views.crearproducto,name='crear'),
    path('hecho/',views.hecho,name='hecho'),
    path('editar/',views.editarproducto,name='editar'),
]
