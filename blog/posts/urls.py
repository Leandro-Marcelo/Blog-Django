from django.urls import path # utilizamos el path para registrar las URLS

#from .views import posts,home,post,create_post,edit_post, delete_post la forma antigua de como lo estaba haciendo

# el . hace referencia a la carpeta actual (posts)
from . import views
# este va de la mano con el namespace
app_name = 'posts'
urlpatterns = [
    # este name nos va a servir para referenciar la route, de esta manera si lo cambiamos, en el template seguirá funcionando porque esta referenciado por el name y no por la route, para ello necesitaremos de una función que será definida en el modelo
    path('', views.posts, name='posts_list'),
    # OJO importantisimo de que este antes del post/<int:id> ya que sino va a entrar ahí primero y nosotros no queremos eso
    path('create', views.create_post, name='post_create'),
    path('<int:id>', views.post, name='post_detail'),
    path('edit/<int:id>', views.edit_post, name='post_edit'),
    path('delete/<int:id>', views.delete_post, name='post_delete')
]
