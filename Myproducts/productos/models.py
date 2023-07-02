from django.db import models

# Modelo llamado Productos

class Productos(models.Model):

    class Meta:
        verbose_name = 'Productos'
        verbose_name_plural = 'Productos'
    
    nombre = models.CharField('Nombre', max_length=100, default='Sin nombre')
    descripcion = models.TextField('Descripción', default='Sin descripción')
    precio = models.DecimalField('Precio', max_digits=8, decimal_places=2, default=0.00)
    fecha_registro = models.DateField('Fecha de registro', auto_now_add=False)
    estatus = models.BooleanField('Estatus', default=True)

    def __str__(self):
        return self.nombre

