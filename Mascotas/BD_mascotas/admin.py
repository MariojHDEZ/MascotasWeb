from django.contrib import admin
from .models import Mascota, Servicio,Producto, MascotaServicio, Usuario, ProductoUsuario, Post, Categoria, Contacto

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('id_mascota', 'tipo', 'raza', 'nom_mas', 'fecha_naci', 'foto', 'id_usuario' )
admin.site.register(Mascota, MascotaAdmin)

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id_servi', 'nom', 'descripcion', 'precio', 'imagen'  )
admin.site.register(Servicio, ServicioAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_pro', 'nom_pro', 'desc_pro', 'precio_pro',  'foto', 'stock' )
admin.site.register(Producto, ProductoAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_persona', 'user', 'pas', 'nom',  'ape', 'dir', 'tel', 'correo', 'tipo', 'foto' )
admin.site.register(Usuario, UsuarioAdmin)

class MascotaServicioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'id_servicio', 'id_mascota', 'fecha_servicio')
admin.site.register(MascotaServicio, MascotaServicioAdmin)

class ProductoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('codpu', 'id_persona', 'id_pro', 'cant', 'total')
admin.site.register(ProductoUsuario, ProductoUsuarioAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido', 'fecha', 'imagen', 'fedicion')
    ordering=('titulo', 'fecha')
    list_filter=('id_persona_id__nom','titulo')
admin.site.register(Post, BlogAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nom','FCreacion')
admin.site.register(Categoria, CategoriaAdmin)

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nom','correo', 'tel', 'apellido')
admin.site.register(Contacto, ContactoAdmin)
