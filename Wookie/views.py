from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from accounts.models import Profile

def main(request):
    objs = Post.objects
    return render(request, 'main.html', {'obj' : objs})

def detail(request, pk, user_id):
    post = get_object_or_404(Post, pk = pk)
    user = get_object_or_404(Profile, pk = user_id)
    return render(request, 'detail.html', {'post':post, 'user':user})

def beauty(request):
    objs = Post.objects
    return render(request, 'beauty.html', {'obj' : objs})

def art(request):
    objs = Post.objects
    return render(request, 'art.html', {'obj' : objs})

def other(request):
    objs = Post.objects
    user = get_object_or_404(Profile, pk = user_id)
    return render(request, 'other.html', {'obj' : objs, 'user':user})

def add_comment(request, pk, user_id):
    post = get_object_or_404(Post, pk = pk)
    author = get_object_or_404(Profile, pk = user_id)
    if request.method == 'POST':
        comment = Comment()
        comment.post = post
        comment.author = author
        comment.body = request.POST['body']
        comment.save()
    return redirect('/Wookie/detail/'+str(post.id)+'/'+str(author.id))

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
