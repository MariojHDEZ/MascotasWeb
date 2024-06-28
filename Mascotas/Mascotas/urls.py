
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views
from BD_mascotas import views as bd
from BD_mascotas.views import BlogListView, Blogcreate, Contactocreate
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.inde, name='index'),
    #path('blog/', bd.blog ,name='blog'),
    
    path('por/', core_views.por, name='portafolio'),
    path('serr', core_views.ser, name='services'),
    path('ingree/', core_views.ingre, name='ingresar'),
     

    path('blog/', BlogListView.as_view(), name='blog'),
    path('Crear/', Blogcreate.as_view(), name='crear'),
    path('con/', Contactocreate.as_view(), name='contacto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)