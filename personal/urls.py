from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartamentoViewSet, EmpleadoViewSet, AsistenciaViewSet, total_empleados

router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'empleados', EmpleadoViewSet)
router.register(r'asistencias', AsistenciaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('total-empleados/', total_empleados),
]
