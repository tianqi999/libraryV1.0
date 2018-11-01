import datetime

from django.http import JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
from library.models import *
import jsonpickle

#显示读者借阅页面
def bookBorrow_view(request):
    if request.method == "GET":
        return render(request,'bookBorrow.html')
    else:
        if request.POST.get("inputkey"):
            bookcode = request.POST.get("inputkey")
            bookname = Bookinfo.objects.get(bookcode=bookcode)
            readername = request.POST.get("readername")
            readername = Readerinfo.objects.get(rname=readername)
            olddate = request.POST.get("olddate")
            olddate = datetime.datetime.strptime(olddate,"%Y-%m-%d")
            newdate = request.POST.get("newdate")
            newdate = datetime.datetime.strptime(newdate,"%Y-%m-%d")
            Borrow.objects.create(rid=readername,bid=bookname,borrowtime=olddate,backtime=newdate)
            return redirect("/book_operation/bookBorrow/")
        return redirect("/book_operation/bookBorrow/")
# 读者信息查询
def getReaderInfo(request):
    # 获取读者条形码
    readerid = request.GET.get('readerid',0)

    readerid = int(readerid)

    # 获取读者信息
    reader = Readerinfo.objects.get(barcode=readerid)
    typename = reader.rtid.typename
    num = reader.rtid.num

    sreader = jsonpickle.dumps(reader,unpicklable=False)

    return JsonResponse({'reader': sreader,'typename':typename,'num':num})

#图书信息查询
def getBookInfo(request):
    f = request.GET.get('f')
    bookcode = request.GET.get('s')
    if f == 'barcode':
        bookcode = int(bookcode)
        bookinfo = Bookinfo.objects.get(bookcode=bookcode)
        bookcase = bookinfo.bcid.bcname
    else:
        bookinfo = Bookinfo.objects.get(bname=bookcode)
        bookcase = bookinfo.bcid.bcname
    sbookinfo = jsonpickle.dumps(bookinfo,unpicklable=False)
    return JsonResponse({'bookInfo':sbookinfo,'bookcase':bookcase})