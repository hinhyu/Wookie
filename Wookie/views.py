from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment, Message
from accounts.models import Profile

def main(request):
    return render(request, 'main.html')

def detail(request, pk, user_id):
    post = get_object_or_404(Post, pk = pk)
    user = get_object_or_404(Profile, pk = user_id)
    return render(request, 'detail.html', {'post':post, 'user':user})

def beauty(request):
    objs = Post.objects.filter(category="beauty")
    return render(request, 'beauty.html', {'obj' : objs})

def art(request):
    objs = Post.objects.filter(category="art")
    return render(request, 'art.html', {'obj' : objs})

def other(request):
    objs = Post.objects.filter(category="other")
    return render(request, 'other.html', {'obj' : objs})

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

def write_message(request, comment_id, user_id):
    return render(request, 'mail.html', {'comment_id':comment_id, 'user_id':user_id})

def send_message(request, comment_id, user_id):
    receiver = get_object_or_404(Profile, pk=comment_id)
    sender = get_object_or_404(Profile, pk=user_id)
    if(request.method == 'POST'):
        message = Message()
        message.sender = sender
        message.receiver = receiver
        message.text = request.POST['body']
        message.save()
    recieved = Message.objects.filter(receiver=sender)
    sent = Message.objects.filter(sender=sender)
    return render(request, 'profile.html', {'recieved':recieved, 'sent':sent})

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
