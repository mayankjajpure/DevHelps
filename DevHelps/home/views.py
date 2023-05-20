from django.shortcuts import render
from .models import BlogModel

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def feeds(request):
    blogs = BlogModel.objects.all().order_by('id')
    context = {'post':blogs}
    return render(request, 'feeds.html',context)

def viewblog(request,slug):
    blogs = BlogModel.objects.filter(slug=slug).first()
    context = {'post':blogs}
    return render(request, 'view.html',context)


