from django.views.generic import ListView
from .models import Producto

class HomeView(ListView):
    model = Producto
    template_name = 'index.html'
    context_object_name = 'productos'