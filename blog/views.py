from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def single(request):
    return render(request, "blog/single_post.html")