from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def cat(request):
    return render(request, 'category.html')


def about(request):
    return render(request, 'about.html')

def cart(request):
    return render(request, 'cart.html')

def lg(request):
    return render(request, 'reg.html')

def home(request):
    return render(request,'home.html')

    
def wl(request):
    return render(request,'wl.html')

def wl2(request):
    return render(request,'wl2.html')

def catlog(request):
    return render(request, 'catlog.html')


def logcart(request):
    return render(request, 'logcart.html')