from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from posts.models import Mascota
from .serializers import MascotaSerializer,PersonaSerializer,MascotaPersonaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class MascotaView(APIView):
    def get(self,request):
        mascotas=Mascota.objects.all()
        serializer=MascotaSerializer(mascotas,many=True)
        return Response(serializer.data)

    def post(self,request):
        codigo = request.POST.get('codigo')
        imagen = request.POST.get('imagen')
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        raza = request.POST.get('raza')
        descripcion = request.POST.get('descripcion')

        mas = Mascota(codigo=codigo,imagen=imagen,nombre=nombre,edad=edad,raza=raza,descripcion=descripcion)
        mas.save()
        return Response()
    
class MascotaFiltro(APIView):
    def get(self,request,filtro):
        mascotas=Mascota.objects.filter(patio=filtro)
        serializer=MascotaSerializer(mascotas,many=True)
        return Response(serializer.data)

    def post(self,request):

        
       return Response()

class PersonaView(APIView):
    def get(self,request):
        personas=Persona.objects.all()
        serializer=PersonaSerializer(personas,many=True)
        return Response(serializer.data)
    
class PersonaFiltro(APIView):
    def get(self,request,filtro):
        personas=Persona.objects.filter(patio=filtro)
        serializer=PersonaSerializer(personas,many=True)
        return Response(serializer.data)

    def post(self,request):
        
       return Response()

class MascotaPersonaView(APIView):
    def get(self,request):
        mascotapersonas=MascotaPersona.objects.all()
        serializer=MascotaSerializer(mascotapersonas,many=True)
        return Response(serializer.data)
    
class MascotaPersonaFiltro(APIView):
    def get(self,request,filtro):
        mascotapersonas=MascotaPersona.objects.filter(patio=filtro)
        serializer=MascotaSerializer(mascotapersonas,many=True)
        return Response(serializer.data)

    def post(self,request):
        
       return Response()           

       