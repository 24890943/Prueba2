from django.shortcuts import render , HttpResponse

# Create your views here.
layout="""
<h1>sitio web con django</h1>
<hr>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    <li>
    <li>
        <a href="/hola-mundo">hola mUndo</a>
    <li>
</ul>

        """

def index(request):
    return HttpResponse(layout+"""<h1> inicio </h1>""")


def holaMundo(request):
    return HttpResponse(layout+"""<h1>hola mundo con django</h1>""")

def inicio(request):
    return HttpResponse(layout+"""<h1> inicio1 </h1>""")

