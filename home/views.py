from django.shortcuts import render,redirect 
from django.http import HttpResponse
from .models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def home(request):
    max=0
    posts=Post.objects.all()
    for post in posts:
        if post.view>max:
            max=post.view
    popular=Post.objects.filter(view=max)[0]
    print(popular) 
    return render(request,"home/home.html",{"popular":popular})

def about(request):
    return render(request,"home/about.html")

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        desc=request.POST['desc']
        c=Contact(name=name,email=email,mobile=mobile,desc=desc)
        if len(name)>3:
            c.save()
            messages.success(request, 'contact request send!!!.')
     
    return render(request,"home/contact.html")

def search(request):
    query=request.GET['query']
    if len(query) >70:
        allPost=[]
       
    else:
        allPostTitle=Post.objects.filter(title__icontains=query)
        allPostContent=Post.objects.filter(content__icontains=query)
        allPostAuthor=Post.objects.filter(author__icontains=query)
        allPost=allPostTitle.union(allPostContent)
        allPost=allPost.union(allPostAuthor)
      
        if len(allPost)==0:
            messages.warning(request, 'required result not present...')

    return render(request,"home/search.html",{"blogs":allPost})



def loginhandle(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return HttpResponse("something went wrong")

def logouthandle(request):
    logout(request)
    return redirect("/")

def registerhandle(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']

        if pass1 == pass2:
            userr=User.objects.create_user(username,email,pass1)
            print(userr)
            userr.first_name=fname
            userr.last_name=lname
            userr.save()
            return redirect("/")
    
    else:
            return HttpResponse("404-something went wrong")
