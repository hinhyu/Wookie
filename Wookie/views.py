from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post1
from .models import Post2
from .models import Post3

def main(request):
    return render(request, 'main.html')

def new(request):
    return render(request, 'new.html')

def create1(request):
    if request.method == 'POST':
        post = Post1()
        post.image = request.FILES['image']
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('/Wookie/'+str(post.id))
    
    else:
        return render(request, 'new.html')

def create2(request):
    if request.method == 'POST':
        post = Post2()
        post.image = request.FILES['image']
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('/Wookie/'+str(post.id))
    
    else:
        return render(request, 'new.html')

def create3(request):
    if request.method == 'POST':
        post = Post3()
        post.image = request.FILES['image']
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('/Wookie/'+str(post.id))
    
    else:
        return render(request, 'new.html')



def edit1(request, pk):
    post = get_object_or_404(Post1, pk = pk)
   
    if request.method == 'POST':
        post.title = request.POST['title']
        post.image = request.FILES['image']
        post.body = request.POST['body']        
        post.save()
        return redirect('/Wookie/'+str(post.id))
    
    return render(request, 'edit.html', {'posts':post})

def edit2(request, pk):
    post = get_object_or_404(Post2, pk = pk)
   
    if request.method == 'POST':
        post.title = request.POST['title']
        post.image = request.FILES['image']
        post.body = request.POST['body']        
        post.save()
        return redirect('/Wookie/'+str(post.id))
    
    return render(request, 'edit.html', {'posts':post})

def edit3(request, pk):
    post = get_object_or_404(Post3, pk = pk)
   
    if request.method == 'POST':
        post.title = request.POST['title']
        post.image = request.FILES['image']
        post.body = request.POST['body']        
        post.save()
        return redirect('/Wookie/'+str(post.id))
    
    return render(request, 'edit.html', {'posts':post})



def delete(request, pk):
    post = get_object_or_404(Post1, pk = pk)
    post.delete()
    return redirect('main')