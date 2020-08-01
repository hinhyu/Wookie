from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment

def main(request):
    return render(request, 'main.html')

def detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'detail.html', {'post':post})

def beauty(request):
    objs = Post.objects.filter(category="beauty")
    return render(request, 'beauty.html', {'obj' : objs})

def art(request):
    objs = Post.objects.filter(category="art")
    return render(request, 'art.html', {'obj' : objs})

def other(request):
    objs = Post.objects.filter(category="other")
    return render(request, 'other.html', {'obj' : objs})

def add_comment(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == 'POST':
        comment = Comment()
        comment.post = post
        comment.body = request.POST['body']
        comment.save()
    return redirect('/Wookie/detail/'+str(post.id))

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        post = Post()
        post.image = request.FILES['image']
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('/Wookie/'+str(post.id))
    
    else:
        return render(request, 'new.html')


def edit(request, pk):
    post = get_object_or_404(Post, pk = pk)
   
    if request.method == 'POST':
        post.title = request.POST['title']
        post.image = request.FILES['image']
        post.body = request.POST['body']        
        post.save()
        return redirect('/Wookie/'+str(post.id))
    
    return render(request, 'edit.html', {'posts':post})


def delete(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.delete()
    return redirect('main')
