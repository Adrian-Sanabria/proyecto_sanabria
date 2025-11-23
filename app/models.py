from django.db import models

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre


class Tramite(models.Model):
    TIPO_CHOICES = [
        ('DNI Nuevo','DNI Nuevo'),
        ('Renovación','Renovación'),
        ('Duplicado','Duplicado'),
        ('Rectificación','Rectificación'),
        ('Pasaporte','Pasaporte'),
        ('Otros','Otros'),
    ]

    ESTADO_CHOICES = [
        ('Pendiente','Pendiente'),
        ('En proceso','En proceso'),
        ('Entregado','Entregado'),
    ]

    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    cliente = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    forma_pago = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    notas = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Pago(models.Model):
    BANCOS = [
        ('BN','Banco de la Nación'),
        ('BBVA','BBVA'),
        ('INTER','Interbank'),
        ('KAS','KasNet'),
    ]

    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    banco = models.CharField(max_length=20, choices=BANCOS)
    monto = models.DecimalField(max_digits=9, decimal_places=2)
    operacion = models.CharField(max_length=100, blank=True)
    dni = models.CharField(max_length=12, blank=True)
    voucher = models.FileField(upload_to='vouchers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Foto(models.Model):
    ENTREGA_CHOICES = [
        ('Impresa','Impresa'),
        ('Digital','Digital'),
        ('Ambas','Ambas')
    ]

    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    cliente = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50)
    archivo = models.ImageField(upload_to='fotos/')
    entrega = models.CharField(max_length=10, choices=ENTREGA_CHOICES)
    monto = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    creado = models.DateTimeField(auto_now_add=True)
