from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista1(request):
    html = """<h3 style="color:brown">Bienvenido a la App2 de la rama 2</h3>
    <main>Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</main>"""
    return HttpResponse(html)

def vista2(request):
    html = """<p style="color:cyan">Lorem Ipsum is simply dummy text of the printing and typesetting industry. </p>
    <ol>1- Hola </ol><ol>2- Como </ol><ol>3- Estás </ol>
    <link>https://www.youtube.com//</link>
    """
    return HttpResponse(html)