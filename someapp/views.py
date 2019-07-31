from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from someapp import models
from someapp import forms
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'someapp/some_form.html')

def add(request):
    print(request.POST)
    print(type(request.POST))
    a=request.POST.get("a")
    b=request.POST.get("b")
    return HttpResponse(int(a)+int(b))

def profile(request):
    name=request.GET.get("name")
    skills=["Java","python","golang","javascript"]
    d={"name":name,"skills":skills}
    return render(request,'someapp/index.html',d)


def submit(request):
    username=request.POST.get("username")
    comment=request.POST.get("comment")

    commentModel=models.Comments(username=username,content=comment)
    commentModel.save()

    commentList=models.Comments.objects.all()

    for i in commentList:
        print(i)
    skills = ["Java", "python", "golang", "javascript"]
    d = {"name": username, "skills": skills,"comment":comment}
    return render(request, 'someapp/index.html', d)


def addComment(request):
    has_commented=request.session.get("has_commented")
    if(not has_commented):
        request.session["has_commented"]=True
        f=forms.CommentForm(request.POST)
        f.save()
        return HttpResponse("success")
    else:
        return HttpResponse("You have already commented")


def showComments(request):

    comments=models.Comments.objects.all()


    d={
        "comments":comments
    }
    return render(request,'someapp/comments.html',d)

def delComment(request):
    comment_id=request.POST.get("comment_id")
    models.Comments.objects.filter(pk=comment_id).delete()
    return HttpResponse("comment deleted")




def login(request):
    if(request.method=="GET"):
        f=forms.LoginForm()
        return render(request,'someapp/login.html',{"form":f})
    else:
        f=forms.LoginForm(request.POST)
        if(f.is_valid()):

            pass
        return
