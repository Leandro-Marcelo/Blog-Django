from django.db import models
""" por ahora lo vamos a imporar simplemente por aprender, sin embargo, python ya tiene convierta la parte de las fechas """
from django.utils import timezone
from django.urls import reverse

# Create your models here.
""" Le estoy diciendo que la clase Post, herede de la clase models.Model de esta forma le estamos indicando que la clase en si misma va a ser un modelo, es decir, que va seguir todos los principios que ya se definieron de la clase superior y que también va a poder hacer uso de todo ello """
class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title") # type chart,  <=> string, para que lo ponga Title en la cabecera de la columna
    description = models.CharField(max_length=100)
    img = models.CharField(max_length=240)
    content = models.TextField() # me permite escribir texto sin limitaciones
    created_at = models.DateTimeField(default=timezone.now) # DateTimeField guarda tanto la fecha como la hora y DateField solo la fecha. Lo que haría Django es ejecutar este método de timezone.now cada vez que creemos un nuevo campo de fecha. Timezone es útil cuando queremos modificarlo, por ejemplo, fecha de entrega sería fecha de hoy mas 7 días y modificamos el valor por defecto, pero otra forma de realizarlo es auto_now=, ahora el auto_now se utiliza para que cada vez que se actualiza hace como el cambio, auto_now_add= es simplemente cuando se crea el elemento. Entonces podemos elegir entre default=timezone.now ó auto_now_add=True

    # definimos el string, o el ToString de algunos u otros lenguajes 
    def __str__(self):
        # strftime convierte a una fecha en string pero con un formato de tiempo
        return f'{self.created_at.strftime("%d/%m/%Y")} {self.title}'
        
    def get_url(self):
        # la pk hace referencia a su id
        return reverse('posts:post_detail', args=[self.pk])


