from django.shortcuts import render
from .models import Category, Post

# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories':categories})

def category_detail(request, slug):
    category = Category.objects.get(slug__exact=slug)
    return render(request, 'category_detail.html', {'category': category})