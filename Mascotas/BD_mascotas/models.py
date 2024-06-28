from django.db import models
from django.utils.timezone import now


# Create your models here.

op=[
    ["felino","felino"],
    ["Canino","Canino"],
    ["Ave","Ave"],
]

class Mascota(models.Model):
    id_mascota = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=45, blank=True, null=True, choices=op)
    raza = models.CharField(max_length=45, blank=True, null=True)
    nom_mas = models.CharField(max_length=45, blank=True, null=True)
    fecha_naci = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to="project",verbose_name="Imagen")
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mascota'

    def __str__(self):
        return f"{self.nom_mas} ({self.tipo})"
    

class MascotaServicio(models.Model):
    codigo = models.IntegerField(primary_key=True)
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio')
    id_mascota = models.ForeignKey(Mascota, models.DO_NOTHING, db_column='id_mascota')
    fecha_servicio = models.ImageField(upload_to="BlogImg", null=True, blank=True, verbose_name="Imagen")
    

    class Meta:
        managed = False
        db_table = 'mascota_servicio'

    def __str__(self):
        return f"{self.id_mascota.nom_mas} - {self.id_servicio.nom}"


class Producto(models.Model):
    id_pro = models.AutoField(primary_key=True)
    nom_pro = models.CharField(max_length=45)
    desc_pro = models.CharField(max_length=45)
    precio_pro = models.FloatField()
    foto = models.ImageField(upload_to="productoImg",verbose_name="Imagen")
    stock = models.FloatField()

    class Meta:
        managed = False
        db_table = 'producto'

    def __str__(self):
        return self.nom_pro


class ProductoUsuario(models.Model):
    codpu = models.IntegerField(db_column='codPU', primary_key=True)  # Field name made lowercase.
    id_persona = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_persona')
    id_pro = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_pro')
    cant = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'producto_usuario'

    def __str__(self):
        return f"{self.id_pro.nom_pro} - {self.id_persona.user}"


class Servicio(models.Model):
    id_servi = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="servicioImg", verbose_name="Imagen")

    class Meta:
        managed = False
        db_table = 'servicio'

    def __str__(self):
        return self.nom

#AGREGAMOS UN DICCIONARIO CON LAS OPCIONES DEL USUARIO

op=[
    [0,"Administrador"],
    [1,"Cliente"],
]


class Usuario(models.Model):
    id_persona = models.IntegerField(primary_key=True)
    user = models.CharField(unique=True, max_length=45, blank=True, null=True)
    pas= models.CharField(db_column='pas', max_length=45, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    nom = models.CharField(max_length=45, blank=True, null=True)
    ape = models.CharField(max_length=45, blank=True, null=True)
    dir = models.CharField(max_length=45, blank=True, null=True)
    tel = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, choices=op)
    foto= models.ImageField(upload_to="BlogImg", null=True, blank=True, verbose_name="Imagen")

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return f"{self.nom} {self.ape} ({self.user})"
    
class Categoria(models.Model):
    nom=models.CharField(max_length=100, verbose_name="Nombre")
    FCreacion=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    class Meta:
        verbose_name="categorias"

    def __str__(self):
        texto="{0}"
        return texto.format(self.nom)

class Post(models.Model):
    titulo=models.CharField(max_length=200, verbose_name="Titulo")
    contenido=models.TextField(verbose_name="Contenido")
    fecha=models.DateTimeField(default=now, verbose_name="facha de publicacion")
    imagen=models.ImageField(upload_to="BlogImg", null=True, blank=True, verbose_name="Imagen")
    id_persona=models.ForeignKey(Usuario, on_delete=models.SET_NULL,null=True)
    categorias=models.ManyToManyField(Categoria, verbose_name="Nombre")
    Fcreacion=models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    fedicion=models.DateTimeField(auto_now=True, verbose_name="fecha de edicion")
     

    class Meta:
        verbose_name="Post"

    def __str__(self):
        texto="{0}"
        return texto.format(self.titulo)
    
class Contacto(models.Model):
    nom = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    tel = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        verbose_name="Contacto"

    def __str__(self):
        texto="{0}"
        return texto.format(self.nom)