from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

# Create your views here.
def home(request):
    post_list = Article.objects.all()  #get all objects of Article
    return render(request, 'home.html', {'post_list' : post_list})