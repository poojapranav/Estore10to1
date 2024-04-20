from django.shortcuts import render,HttpResponse,redirect
from messageapp.models import Msg
# Create your views here.
def testing(request):
    return HttpResponse("hello linked successfully")
def create(request):
    print("request is:",request.method)
    if request.method=="GET":
        return render(request,'create.html')
    else:
        #fetch data from form
        n=request.POST['uname']
        e=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        print("name:",n)
        print("email:",e)
        print("mobile:",mob)
        print("message:",msg)
        #insert
        m=Msg.objects.create(name=n,email=e,mobile=mob,msg=msg)
        m.save()
        #return HttpResponse("data inserted successfully")
        return redirect('/dashboard')
def dashboard(request):
    m=Msg.objects.all()
    print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)
    #return HttpResponse("data is feched successfully")
def delete(request,rid):
    # print("id to be deleted:",rid)
    # return HttpResponse("id yto be deleted:"+rid)
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')
def edit(request,rid):
    # print("id to be edited:",rid)
    # return HttpResponse("id yto be edited:"+rid)
    d=Msg.objects.get(id=rid)
    if request.method=='POST':
        n=request.POST['uname']
        e=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        print("name:",n)
        print("email:",e)
        print("mobile:",mob)
        print("message:",msg)
        k=Msg.objects.filter(id=rid).update(name=n,email=e,mobile=mob,msg=msg)
        return redirect('/dashboard')
    print(d)
    context={}
    context['data']=d
    return render(request,'edit.html',context)

