from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Post

# Create your views here.

def posts(req):
  posts = Post.objects.all() # SELECT * FROM posts
  print(posts) # nos retorna un QuerySet, es decir, un conjunto de datos
  return HttpResponse("Hi There, in this video I'm gonna create new Project using Django")
