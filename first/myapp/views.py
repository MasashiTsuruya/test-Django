from django.shortcuts import render
import os

# Create your views here.
name = os.getlogin()
def index(request):
    """/ トップページ """
    context = {
    'name': name
    }
    return render(request, 'myapp/index.html', context)

def about(request):
    """/about アバウトページ """
    return render(request, 'myapp/about.html')

def info(request):
    """/info infoページ"""
    return render(request, 'myapp/info.html')
