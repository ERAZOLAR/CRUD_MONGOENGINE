from flask import Flask, render_template, redirect, request, session
# from pymongo import MongoClient
# import yagmail
from flask_mongoengine import MongoEngine
# from flask.json import JSONEncoder

from mongoengine.errors import NotUniqueError

from models.model import USUARIOS, CATEGORIAS, PRODUCTOS

# import pymongo


# ALTERNATIVA DE CONEXION



# SE CREA APLICACION
app = Flask(__name__)
#app.json = {'ensure_ascii': False}
app.secret_key = "mxynkmdclqtnmmmk"
#CREAMOS CLAVE PARA INICIO SESION EN FLASK ... NO SE LOGRA INGRESO DIGITANDO CORREO Y PASSWORD



app.config["UPLOAD_FOLDER"]="./static/imagenes"

#CREO CONEXXION A MONGO ENGINE

app.config['MONGODB_SETTINGS'] = [{
    "db": "GESTIONPRODUCTOS",
    "host": "localhost",
    "port": 27017
}]



db = MongoEngine(app)

# try:
#     user = USUARIOS()
#     user.usuario = 'FF'
#     user.password = '12345'
#     user.nombres = 'Federico Figueroa'
#     # user.apellidos = 'Figueroa'
#     user.correo = 'federicofigueroa@gmail.com'
#     #user.save()
# except NotUniqueError as e:
#     print('Usuario / Correo ya existen') 






#CREO CONEXION A MONGOCOMPASS .... OTRA FORMA MAS CORTA 
#miConexion=pymongo.MongoClient("mongodb://localhost:27017")



#CREO TODAS ESTAS LINEAS
# client = MongoClient("mongodb://localhost:27017/")
# db = client["GESTIONPRODUCTOS"]
# usuarios = db["USUARIOS"]
# categorias = db["CATEGORIAS"]  
# productos = db["PRODUCTOS"] 


#CREO CONEXION A MONGOATLAS  .... SE VERIFICAN CRDENCOIALES ... NO HAY CONEXION !!!!
#miConexion=pymongo.MongoClient('mongodb+srv://burritavenzo:Apolo3128289640@cluster0.w5qlfso.mongodb.net/')
#HACER CONEXION CON MONGO ATLAS



# ESTOS INICIALMENTE  **
#SE CREA CONEXION CON BASEDATOS
#baseDatos = miConexion["GESTIONPRODUCTOS"]

# SE LLAMAN A COLECCIONES DE BASEDATOS CON METODO ALTERNATIVO DE CONEXION 
#categorias = baseDatos["CATEGORIAS"]
#productos = baseDatos["PRODUCTOS"]
#usuarios=baseDatos['USUARIOS']

# IMPORTAMOS ARCHIVOS DENTRO CARPETA CONROLADOR
from controlador.productoController import *
from controlador.categoriaController import *







# DAMOS ARRANQUE App EN PUERTO 3000
if __name__=="__main__":
    app.run(port=3000,  debug=True)    
