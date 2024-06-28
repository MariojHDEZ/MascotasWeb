from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Post, Contacto
from django.views.generic import ListView, CreateView
from .forms import BlogForms, ContactoForms
from django.urls import reverse_lazy


"""def blog(request):
    post=Post.objects.all()
    return render(request, "BD_mascotas/blog.html",{'blog':post})"""

#CBV EN LA CRUD: LISTVIEW-POST Y CATEGORIA DEL TEMPLATE BLOG

class BlogListView(ListView):
    model=Post
    paginate_by=1
    

    def get_queryset(self):
        return Post.objects.all()
    
    #envia informacion adicioanal para poder paginar 
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return context
    
#CBV EN LA CRUD: LISTVIEW-POST Y CATEGORIA DEL TEMPLATE BLOG
class Blogcreate(CreateView):
    model=Post#tabla
    form_class= BlogForms
    template_name='core/createBlog.html'
    success_url=reverse_lazy('ListarPost')

class Contactocreate(CreateView):
    model= Contacto#tabla
    form_class= ContactoForms
    template_name='core/contact.html'
    success_url=reverse_lazy('contacto')

"""def blog(request):
    post=Post.objects.all()
    return render(request, "BD_mascotas/blog.html",{'blog':post})"""



