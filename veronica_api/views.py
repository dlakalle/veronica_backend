# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from veronica_api.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class BotView(APIView):
    permission_classes = (AllowAny, )

    asignaturas = {
        "economia": [
            "La próxima evaluación es en dos semanas",
            "También tienes una tarea en equipo sobre la elasticidad de la demanda.",
            "Tu promedio actualmente es un 5.2"
        ],
        "matematicas financieras": [
            "No tienes evaluaciones calendarizadas.",
            "El profesor fijó fecha de examen para el próximo mes",
            "En el examen entran todas las unidades, excepto los estados financieros.",
            "Tu promedio actualmente es un 3.9"
        ],
        "contabilidad": [
            "Has aprobado este curso",
            "Tu promedio final es de un 6.4, Felicidades!"
        ],
        "ingles": [
            "Tienes una interrogación oral mañana, es sobre second conditional y third conditional.",
            "Tu promedio actualmente es un 5.5"
        ],
        "elementos de algebra": [
            "Este curso aparece como reprobado.",
            "Tu promedio final es de un 3.8",
        ]
    }

    def post(self, request, format=None):
        content = {}
        print request.data["queryResult"]["parameters"]
        print request.data["queryResult"]["intent"]

        intent = request.data["queryResult"]["intent"]["displayName"]

        if intent == u'asignaturas':
            params = request.data["queryResult"]["parameters"]
            respuesta = self.asignaturas[params["Asignaturas"]]
            content["fulfillmentText"] = "Esto es lo que pude averiguar:"
            content["fulfillmentMessages"] = [
                {
                    "text": {
                      "text": respuesta
                    }
                }
            ]
        else:
            pass
        return Response(content)
