#encodign:utf-8

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
#Para ejecutar ordenes del sistema.
import os

def index(request):
    ahora = datetime.datetime.now()
    t = get_template('index.html')
    #Haciendo Context establezco una variable para que coja los datos la plantilla detail.html
    html = t.render(Context({'fecha_actual': ahora}))
    return HttpResponse(html)


def funciones(request):
    ahora = datetime.datetime.now()
    t = get_template('funciones.html')
    #Haciendo Context establezco una variable para que coja los datos la plantilla detail.html
    html = t.render(Context({'fecha_actual': ahora}))
    return HttpResponse(html)


def mostrarEquiposConectados(request):


    '''
        En esta funcion se llamara al script de ansible que comprueba la conectividad de las maquinas.
    '''
    os.system('ls')

    t = get_template('mostrarEquiposConectados.html')
    html = t.render(Context({}))
    return HttpResponse(html)
