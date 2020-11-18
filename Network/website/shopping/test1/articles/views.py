from django.http import response
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('data')
    return render(request,"articles/article_list.html",{'articles':articles})

def article_detail(request,slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    #return HttpResponse(article.title)
    return render(request,'articles/article_detail.html',{'article':article})