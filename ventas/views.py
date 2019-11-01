from django.shortcuts import render, get_object_or_404
from .models import Catalogo
from django.views import generic
from .forms import CrearForm
# Create your views here.
def index(request):
 
    num_catalogo=Catalogo.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_catalogo':num_catalogo},
    )

class CatalogoListView(generic.ListView):
    model = Catalogo
    paginate_by = 10

class CatalogoDetailView(generic.DetailView):
    model = Catalogo


def crearproducto(request):
	if request.method =='POST':
		form = CrearForm(request.POST)
		if form.is_valid():
			form.save()
		return render(request,'ventas/hecho.html')
	else:
		form = CrearForm()

		return render(request,'ventas/crear.html',{'form':form})

def hecho(request):
    return render(request,'ventas/hecho.html')


def editarproducto(request):
    if request.method == "POST":
        form = CrearForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
    else:
        form = CrearForm()
    return render(request, 'ventas/editar.html', {'form': form})
