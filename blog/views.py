from django.shortcuts import render  
from	.models	import	Post	

def	post_list(request):	
    posts	=	Post.objects.all().order_by('-created_at')	
    return	render(request,	'blog\post_list.html',	{'posts':	posts})

# Create your views here.
def detail_post(request, id):
    post=Post.objects.get(id=id)
    return	render(request,	'blog\post_detail.html',	{'post':	post})

def home(request):
    return render(request, 'blog/index.html')

def blog(request):
    return render(request, 'blog/blog.html')
