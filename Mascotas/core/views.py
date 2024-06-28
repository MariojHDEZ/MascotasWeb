from django.shortcuts import render, HttpResponse
from django.template import loader
from BD_mascotas.models import Servicio, Producto
 


# Create your views here.



def cont(request):
    template=loader.get_template('core/contact.html')
    return HttpResponse(template.render())

def inde(request):
    template=loader.get_template('core/index.html')
    return HttpResponse(template.render())

def por(request):
    port=Producto.objects.all()
    template=loader.get_template('core/portfolio.html')
    return HttpResponse(template.render({"porti":port}))

def ser(request):
    servicios = Servicio.objects.all()
    
    template=loader.get_template('core/services.html')
    return HttpResponse(template.render({"servi":servicios}))

def bas(request):
    template=loader.get_template('core/base.html')
    return HttpResponse(template.render())

def ingre(request):
    template=loader.get_template('core/registro.html')
    return HttpResponse(template.render())



