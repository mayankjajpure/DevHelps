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
    blogs = BlogModel.objects.all().order_by('-id')
    context = {'post':blogs}
    return render(request, 'feeds.html',context)

def viewblog(request,slug):
    blogs = BlogModel.objects.filter(slug=slug).first()
    context = {'post':blogs}
    return render(request, 'view.html',context)

from .forms import AddBLog
def AddBlog(request):
    form = AddBLog()
    if request.method == "GET":
        return render(request, 'addblog.html',{'form':form})
    
    elif request.method == "POST":
        blogobj = BlogModel()
        blogobj.user = request.user
        blogobj.title = request.POST["title"]
        blogobj.image = request.POST["image"]
        blogobj.subtitle = request.POST["subtitle"]
        blogobj.content = request.POST["content"]
        
        print("\n \n \n\n\n  GOT",blogobj)
        blogobj.save()
        return feeds(request)
        