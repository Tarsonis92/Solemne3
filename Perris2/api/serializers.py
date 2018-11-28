from posts.models import Persona,Mascota,MascotaPersona
from rest_framework import serializers

class MascotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mascota
        fields = {'codigoMascota',
                  'imagen',
                  'nombreMascota',
                  'razaMascota',
                  'descripcion',
                  'estadoMascota',
}

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = {
            'nombrePersona',
            'apellidoPersona',
            'fechaNacimiento',
            'numeroFono',
            'regionPersona',
            'ciudadPersona',
            'viviendaPersona',
            'email',
        }

class MascotaPersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MascotaPersona
        fields = {
            'codigoMascota',
            'codigoPersona'
        }        