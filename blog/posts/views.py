from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Post

# Create your views here.

def posts(req):
  posts = Post.objects.all() # SELECT * FROM posts
  print(posts) # nos retorna un QuerySet, es decir, un conjunto de datos, en este caso retorna <QuerySet[<Post:04/05/2022 Mi primera publicación]> esta retornando objetos de tipo post junto con su toString
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
    post = Post(
      title=req.POST['title'],
      description=req.POST['description'],
      img=req.POST['image'],
      content=req.POST['content']
    )

    post.save()

    return redirect("/posts")
    
  return render(req, 'posts/create.html')
  