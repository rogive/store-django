from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
  def __init__(self, nombre, apellido):
    self.nombre=nombre
    self.apellido=apellido

def saludo(request):
  p1=Persona("Mario", "Ramirez")
  temas=["item1", "item2", "item3", "item4", "item5", "item6"]
  fecha_actual=datetime.datetime.now()

  #doc_externo = get_template("plantillauno.html")
  #documento=doc_externo.render({"name": p1.nombre, "apellido": p1.apellido, "fecha_actual": fecha_actual, "temas": temas})
  return render(request, "plantillauno.html", {"name": p1.nombre, "apellido": p1.apellido, "fecha_actual": fecha_actual, "temas": temas})

def antiguedades(request):
  return render(request, "Antiguedades.html", {"name_person": "pedrito"})

def saludar(request):
  p1=Persona("Juan", "Perez")
  temas=["item1", "item2", "item3", "item4", "item5", "item6"]
  fecha_actual=datetime.datetime.now()
  doc_externo=open("C:/Users/natik/Dropbox/Fullstack/projects/django/categories_django/categories_django/templates/plantillauno.html")
  plt=Template(doc_externo.read())
  doc_externo.close()
  ctx=Context({"name": p1.nombre, "apellido": p1.apellido, "fecha_actual": fecha_actual, "temas": temas})

  documento=plt.render(ctx)

  return HttpResponse(documento)

def despedida(request):
  return HttpResponse("Adios Amig@")

def getDate(request):
  fecha_actual=datetime.datetime.now()
  documento="""
    <html>
      <body>
        <h1>Fecha y hora actuales %s
        </h1>
      </body>
    </html>""" % fecha_actual
  return HttpResponse(documento)

def getAge(request, edad, year):
  periodo = year - 2020
  edadFutura = edad + periodo
  documento = """
    <html>
      <body>
        <h1>En el año %s tendrás %s años</h1>
      </body>
    </html>""" %(year, edadFutura)
  return HttpResponse(documento)