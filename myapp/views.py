from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import forms
# Create your views here.


def check(request):
    sess=request.session.get("c")
    if(not sess):
        sess="a"
    else:
        sess=sess+"a"
        request.session["c"]=sess
    return HttpResponse(sess)

def submit(request):
    post_data=request.POST
    f=forms.AuthenticationForm(post_data)
    if(f.is_valid()):
        return HttpResponseRedirect("myapp/profile/")
    return render(request,'myapp/login.html')




def profile(request):
    d = {
        "title": "Profile",
        "myname": "Bhargab",
        "langs":[
            "Java",
            "Python",
            "C/C++",
            "JavaScript",
            "Golang"
        ]

    }

    return render(request, 'myapp/profile.html',d)