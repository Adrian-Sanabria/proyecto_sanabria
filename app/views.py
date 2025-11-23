from rest_framework import viewsets, filters
from .models import Sucursal, Tramite, Pago, Foto
from .serializers import SucursalSerializer, TramiteSerializer, PagoSerializer, FotoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count

class SucursalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    permission_classes = [IsAuthenticated]

class TramiteViewSet(viewsets.ModelViewSet):
    queryset = Tramite.objects.all().order_by('-created_at')
    serializer_class = TramiteSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['cliente', 'tipo']

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all().order_by('-created_at')
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]

class FotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all().order_by('-creado')
    serializer_class = FotoSerializer
    permission_classes = [IsAuthenticated]

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        data = {
            "tramites_total": Tramite.objects.count(),
            "ingresos_tramites": Tramite.objects.aggregate(Sum('monto'))['monto__sum'],
            "ingresos_pagos": Pago.objects.aggregate(Sum('monto'))['monto__sum'],
            "ingresos_fotos": Foto.objects.aggregate(Sum('monto'))['monto__sum'],
        }
        return Response(data)
