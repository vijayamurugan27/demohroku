from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm



def home(request):
    product = Product.objects.all()
    context = { 'product' : product}
    return render(request,'home.html', context)

def product(request):
    return render(request,'product.html')

def service(request):
    return render(request,'service.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contact.html')



def get_product(request): #create view
    if request.method =="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = ProductForm()
    return render(request, "form.html", {'form': form})


def detail_product(request, pk): # detail view
    product = Product.objects.get(pk = pk)
    context = {"product" :product}
    return render(request, "detail.html", context)



def update_product(request,pk):
    product = Product.objects.get(pk = pk)
    form = ProductForm(request.POST or None, instance =product)
    if form.is_valid():
        form.save()
        return redirect('home')
    
    context = {'product':product, "form":form}
    return render(request, "update.html", context)

def delete_product(request, pk): # detail view
    product = Product.objects.get(pk = pk)
    context = {"product" :product}
    if request.method =='POST':
        product.delete()
        return redirect('home')
    return render(request, "delete.html", context)




from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView


class Productreg(CreateView):
	model = Product
	fields = '__all__'
	template_name = 'CBV/Productreg.html'
	success_url ="/"

class ProductList(ListView):
	model = Product
	template_name = 'CBV/ProductList.html'


class ProductDetail(DetailView):
	model =Product
	template_name = 'CBV/ProductDetail.html'

class ProductUpdate(UpdateView):
	model = Product
	fields = "__all__"
	template_name = 'CBV/ProductUpdate.html'
	success_url ="/"



class ProductDelete(DeleteView):
	model = Product
	template_name = 'CBV/ProductDelete.html'
	success_url ="/"

