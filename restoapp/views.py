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