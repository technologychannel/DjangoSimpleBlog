from django.shortcuts import render

blogs = [
    {'id': 1, 'title': 'How to Learn Computer Basic?', 'content': 'A Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias porro aspernatur voluptates dignissimos iste recusandae quaerat aliquid totam ea delectus excepturi atque quis accusantium explicabo ratione veritatis accusamus, nesciunt nam.'},
    {'id': 2, 'title': 'How to Learn Django?', 'content': 'B Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias porro aspernatur voluptates dignissimos iste recusandae quaerat aliquid totam ea delectus excepturi atque quis accusantium explicabo ratione veritatis accusamus, nesciunt nam.'},
    {'id': 3, 'title': 'How to Get Job As Python Developer', 'content': 'C Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias porro aspernatur voluptates dignissimos iste recusandae quaerat aliquid totam ea delectus excepturi atque quis accusantium explicabo ratione veritatis accusamus, nesciunt nam.'},
]

# Create your views here.
def index(request):
    content = {
        'posts': blogs
    }
    return render(request, "blog/index.html", context=content)

def single(request, postid):
    post = None
    for blog in blogs:
        if blog['id'] == postid:
            post = blog
            break
    return render(request, "blog/single_post.html",{'post': post})