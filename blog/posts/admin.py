from django.contrib import admin
from .models import Post

# aca va la configuración para que aparezca en el panel de administración
# Register your models here.

# esto se lee, Hey sitio de administración, registra el Modelo de Post en el Sitio de  
# admin.site.register(Post)

# Hasta acá esto es como un registro rapido, pero si yo quiero que en la tablita me muestre mas campos

# Si yo quiero que me muestre mas campos, es decir, el title, la description, created_at, yo puedo confiugarlo
# Una vez ya creado la clase PostAdmin, debemos de registrarlo. Registra el modelo de post con todas las propiedades pero aparte le añade la configuración que nosotros agreguemos a la clase. Hay mas partes que podemos modificar pero ya llegaremos ahí. Esto es algo que nosotros conocemos @ como Decorator, lo que hace es que cuando nosotros cuando le pasamos este archivo al Framework Django, va a detectar todas las anotaciones que nosotros tengamos. Por ejemplo, cuando nosotros tengamos una anotación relacionada con el panel de administración lo que hará es agregar código a la clase que tenemos aquí abajo, es decir, aparte de que herede propiedades de admin.modelAdmin le vamosa decir que agregue código que necesita esta clase para mostrarse en el panel de administración. Los Decorator lo que hacen es agregar código, o auto generar código, los decoradores van muy relacionado con la autogeneración de código, en este caso para la clase de abajo 
@admin.register(Post)
# Que PostAdmin herede de admin.ModelAdmin para ahora utilizar el atributo list_display y modificarlo
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'description', 'created_at')  # puede recibir una lista o una tupla, es mas común ver una tupla