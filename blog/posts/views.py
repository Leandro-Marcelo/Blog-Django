from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Post

# Create your views here.

def posts(req):
    # SELECT * FROM posts
    posts = Post.objects.all().order_by("-created_at", "-id") # si -created_at no lo ordena bien, podemos aplicar otro order_by, por ejemplo, por el id de forma descendiente lo que hará es reemplazar el anterior, poner comma y concatenarlo servirá para desempatar el ordenamiento anterior 
    # print(posts) nos retorna un QuerySet, es decir, un conjunto de datos, en este caso retorna <QuerySet[<Post:04/05/2022 Mi primera publicación]> esta retornando objetos de tipo post junto con su toString
    #return HttpResponse("Hi There, in this video I'm gonna create new Project using Django")
    return render(req, 'posts/posts.html', {
        'posts': posts
    }) # le pasamos la request porque así desde el template vamos a poder acceder a cosas como la session, detalles ya en si mismo del usuario. Una manera de pasarle los posts, context=posts, o la otra forma es pasandoselo dentro de un diccionario {'posts':posts}

def home(req):
    return render(req, 'home.html') 

def post(req, id):
    post = Post.objects.get(id=id) # podemos usar filter pero nos va a devolver un array/lista porque va a filtrar entre todos los elementos

    return render(req, 'posts/post.html', {
        'post': post
    })

def create_post(req):
    if req.method == "POST":
        # como POST es un diccionario, puedo acceder a su atributos con esta notación, POST['title']
        post = Post(
        title=req.POST['title'],
        description=req.POST['description'],
        img=req.POST['image'],
        content=req.POST['content'],
        # Django nos agrega dos campos al momento de hacer un foreignkey, author y author id,
        # mientras que en author debemos pasarle tódo el objeto de author, en author id, solo le pasamos su id
        author_id = req.user.pk
        # author = req.user esa es la otra forma de pasarlo

        )
        # me permite almacenar este new post en la base de datos
        post.save() 

        return redirect("/posts")
        
    return render(req, 'posts/create.html')

def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":

        post.title = request.POST['title']
        post.description = request.POST['description']
        post.img = request.POST['image']
        post.content = request.POST['content']


        post.save()

        return redirect("/posts")

    return render(request, 'posts/edit.html', {'post': post})
  
def delete_post(request,id):
    post = Post.objects.get(id=id)

    post.delete()
    return redirect("/posts")