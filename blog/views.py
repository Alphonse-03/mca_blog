from django.shortcuts import render,redirect
from .models import Post,Comments
from django.contrib import messages
from blog.templatetags import extras
# Create your views here.
def blog(request):
    allBlog=Post.objects.all()
    content={"blogs":allBlog}
    return render(request,"blog/blog.html",content)



def blogpost(request,slug):
    variable=Post.objects.filter(slug=slug).first()
    variable.view=variable.view+1
    variable.save()
    comments=Comments.objects.filter(post=variable,parent=None)
    replys=Comments.objects.filter(post=variable).exclude(parent=None)
    replyDict={}
    for reply in replys:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    return render(request,"blog/blogpost.html",{'blog':variable,'comments':comments,'user':request.user,"replys":replyDict})



def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        if len(comment)!=0:
            user=request.user
            postSno=request.POST.get("postno")
            post=Post.objects.get(sno=postSno)
            parentSno=request.POST.get("parentsno")
            reply={}
            if parentSno == "":
                comment= Comments(comment=comment,user=user,post=post)
                comment.save()
                messages.success(request,"comment added")
            else:
                parent=Comments.objects.get(sno=parentSno)
                comment=Comments(comment=comment,user=user,post=post,parent=parent)
    
                comment.save()
                messages.success(request,"your reply success")
            return redirect(f"/blog/{post.slug}")
        else:
            messages.warning(request,"can't post an empty comment")
        return redirect("/blog")
    