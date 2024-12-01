from django.shortcuts import render
#from django.views.generic import TemplateView
from django.views.generic import TemplateView, ListView
#from django.views.generic.edit import CreateView
#from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#kadai_010 DetailViewクラスのimport
from django.views.generic.detail import DetailView
from .models import Product
from django.urls import reverse_lazy

# Create your views here.
class TopView(TemplateView):
  template_name = "top.html"

class ProductListView(ListView):
  model = Product
  paginate_by = 3

class ProductCreateView(CreateView):
  model = Product
  fields = '__all__'

class ProductUpdateView(UpdateView):
  model = Product
  fields = '__all__'
  template_name_suffix = '_update_form'

class ProductDeleteView(DeleteView):
  model = Product
  success_url = reverse_lazy('list')

#kadai_010 DetailViewを継承したクラスを追加
class ProductDetailView(DetailView):
  model = Product