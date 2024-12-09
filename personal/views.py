from rest_framework import viewsets
from .models import Departamento, Empleado, Asistencia
from .serializers import DepartamentoSerializer, EmpleadoSerializer, AsistenciaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

@api_view(['GET'])
def total_empleados(request):
    total = Empleado.objects.count()
    return Response({"total_empleados": total})
