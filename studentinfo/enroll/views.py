from django.shortcuts import render,HttpResponseRedirect

from .forms import studentinfo

from .models import User

# Create your views here.

# for adding and showing student
def add_show(request):
    if request.method == "POST":
        fm=studentinfo(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['Course']
            dw=fm.cleaned_data['div']
            rn=fm.cleaned_data['rollno']
            newst=User(name=nm,email=em,Course=pw,div=dw,rollno=rn)

            newst.save()
            fm=studentinfo()
    else:
        fm=studentinfo()
    stud=User.objects.all()
    return render(request,'enroll/add.html' , {"form":fm,
    "stu":stud})


# for update student

def update_std(request,id):
    if request.method=="POST":
        pi= User.objects.get(pk=id)
        fm=studentinfo(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:

        pi= User.objects.get(pk=id)
        fm=studentinfo(instance=pi)

    return render(request,"enroll/update.html",{"form":fm})





# for deleting students

def del_stud(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')