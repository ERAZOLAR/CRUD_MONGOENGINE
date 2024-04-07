from mongoengine import Document, ReferenceField, StringField, IntField, EmailField
from mongoengine import *

#CREAR LA CLASE QUE REPRESENTA COLECCION USUARIO EN BASEDATOS
class USUARIOS(Document):
    usuario = StringField( max_length=50, required=True, unique=True)
    password = StringField(max_length=50)
    nombres = StringField(max_length=50)
    # apellidos = StringField(max_length=50)
    correo = EmailField(required = True, unique=True)


#CREAR CLASE QUE REPRESENTA LA COLECCION CATEGORIA EN BASE DATOS
class CATEGORIAS(Document):
    nombre = StringField(max_length=50, unique=True)

#CREAR CLASE QUE REPRESENTA LA COLECCION PRODUCTO EN BASE DATOS
class PRODUCTOS(Document):
    codigo = IntField(unique=True)
    nombre = StringField(max_length=50)
    precio = IntField()
    categoria = ReferenceField(CATEGORIAS)

