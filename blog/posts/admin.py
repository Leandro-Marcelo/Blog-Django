from django.contrib import admin
from .models import Post

""" aca va la configuración para que aparezca en el panel de administración """
# Register your models here.

""" esto es como un registro rapido, pero si yo quiero que en la tablita me muestre mas campos """
# admin.site.register(Post)

""" registra el modelo de post con todas las propiedades pero aparte  """
""" el @ es un Decorator, nosotros cuando le pasamos este archivo al Framework de Django, va a notar todas las anotaciones que tengamos Aparte de heredar de admin.ModelAdmin """
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'description', 'created_at')  # puede recibir una lista o una tupla, es mas común ver una tupla