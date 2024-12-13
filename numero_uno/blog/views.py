from django.shortcuts import render
from django.http import HttpResponse

posts = [
  {
    'author' : 'ashimS',
    'title' : 'myfirstblog',
    'content': "laudahunucontent",
    'date' : 'december'
  },
  {
    'author' : 'ashimD',
    'title' : 'mysecondblog',
    'content': "laudahunucontent",
    'date' : 'december'
  }

]

def home(request):
  context= {
    'posts': posts
  }
  return render(request,'blog/home.html',context)

def about(request):
  return render(request,'blog/about.html',{'title': "about"})

