from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from library.models import *
import datetime
def library_modify_view(request):
    if request.method == "GET":
        LibraryInfo = Library.objects.all()
        # for i in LibraryInfo:
        #     print(i.libraryname)
        # print(LibraryInfo)
        return render(request,'library_modify.html',{"LibraryInfo":LibraryInfo})
    else:
        libraryname = request.POST.get("libraryname","")
        curator = request.POST.get("curator","")
        tel = request.POST.get("tel","")
        address = request.POST.get("address","")
        email = request.POST.get("email","")
        url = request.POST.get("url","")
        cd = request.POST.get('createdate','')
        createdate = datetime.datetime.strptime(cd,'%Y-%m-%d')
        introduce = request.POST.get("introduce","")
        Library.objects.filter(id=request.POST.get("id")).update(libraryname=libraryname,curator=curator,tel=tel,address=address,email=email,url=url,createdate=createdate,introduce=introduce)
        return redirect('/sys_settings/library_modify/')

def manager_view(request):
    manager = Manager.objects.all()
    # print(manager)
    return render(request,"manager.html",{"manager":manager})

def manager_del_view(request,mid):
    Manager.objects.filter(id=mid).delete()
    manager = Manager.objects.all()
    # print(manager)
    return render(request,"manager.html",{"manager":manager})


def manager_add_view(request):
    if request.method == "GET":
        return render(request,"manager_add.html")
    else:
        def func(a):
            if a == "on":
                return 1
            else:
                return 0
        user = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        sysset = request.POST.get("sysset")
        sysset = func(sysset)
        # print(sysset)
        readerset = request.POST.get("reader_set")
        readerset = func(readerset)
        library_set = request.POST.get("library_set")
        library_set = func(library_set)
        library_borrow_back = request.POST.get("library_borrow_back")
        library_borrow_back = func(library_borrow_back)
        sys_query = request.POST.get("sys_query")
        sys_query = func(sys_query)
        list1 = []
        for i in Manager.objects.all():
            list1.append(i.user)
        if user in list1:
            return HttpResponse("用户名已存在,请返回上一级")
        else:
            Manager.objects.create(user=user,pwd=pwd,sysset=sysset,readerset=readerset,bookset=library_set,borrowset=library_borrow_back,sysquery=sys_query)
            return redirect("/sys_settings/manager/")


def perset_view(request,pid):
    if request.method == "GET":
        manager = Manager.objects.filter(id=pid).all()
        return render(request,"manager_update.html",{"manager":manager})
    else:
        def func(a):
            if a == "on":
                return 1
            else:
                return 0

        sysset = request.POST.get("sysset")
        sysset = func(sysset)
        # print(sysset)
        readerset = request.POST.get("reader_set")
        readerset = func(readerset)
        library_set = request.POST.get("library_set")
        library_set = func(library_set)
        library_borrow_back = request.POST.get("library_borrow_back")
        library_borrow_back = func(library_borrow_back)
        sys_query = request.POST.get("sys_query")
        sys_query = func(sys_query)
        Manager.objects.filter(id=pid).update(sysset=sysset,readerset=readerset,bookset=library_set,borrowset=library_borrow_back,sysquery=sys_query)
        return redirect("/sys_settings/manager/")

def parameter_modify_view(request):
    if request.method == "GET":
        allpar = Readertype.objects.all()
        count = request.GET.get("key",int(allpar.first().rtid))
        rt = Readertype.objects.get(rtid=count)
        return render(request,"parameter_modify.html",{"allpar":allpar,'rt':rt})
    else:
        num = request.POST.get("cost")
        cprice = request.POST.get("price")
        validity = request.POST.get("validity")
        Readertype.objects.filter(rtid=request.POST.get("id")).update(num=num,cprice=cprice,validity=validity)
        return redirect("/sys_settings/parameter_modify/")

def bookcase_view(request):
    bookcase = Bookcase.objects.all()
    return render(request,"bookcase.html",{"bookcase":bookcase})

def bookcase_add_view(request):
    if request.method == "GET":
        return render(request,'bookcase_add.html')
    else:
        bcname = request.POST.get("uname")
        list1 = []
        for i in Bookcase.objects.all():
            list1.append(i.bcname)
        if bcname in list1:
            return HttpResponse("用户名已存在,请返回上一级")
        else:
            Bookcase.objects.create(bcname=bcname)
            return redirect("/sys_settings/bookcase/")

def bookcase_del_view(request,bid):
    Bookcase.objects.filter(bcid=bid).delete()
    bookcase = Bookcase.objects.all()
    return render(request,"bookcase.html",{"bookcase":bookcase})


def bookcase_update_view(request,buid):
    if request.method == "GET":
        bcname = Bookcase.objects.filter(bcid=buid).all()
        return render(request,"bookcase_update.html",{"bcname":bcname})
    else:
        bcname = request.POST.get("uname")
        Bookcase.objects.filter(bcid=buid).update(bcname=bcname)
        return redirect("/sys_settings/bookcase/")


def getManagerName_view(request):
    managername = request.GET.get("ManagerName")
    list1 = []
    for i in Manager.objects.all():
        list1.append(i.user)
    if managername in list1:
        return JsonResponse({"flag":False})
    else:
        return JsonResponse({"flag": True})


def getBookcase_view(request):
    bookcasename = request.GET.get("Bookcase")
    list1 = []
    for i in Bookcase.objects.all():
        list1.append(i.bcname)
    if bookcasename in list1:
        return JsonResponse({"flag": False})
    else:
        return JsonResponse({"flag": True})