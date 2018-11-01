import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from library.models import *
from django.http import HttpResponse, JsonResponse


# Create your views here.
def page_num(num,size):
    num = int(num)
    paginator = Paginator(Bookinfo.objects.filter(isdelete=0).order_by('bname'),size)
    if num < 1:
        num = 1
    if num > paginator.num_pages:
        num = paginator.num_pages
    start = ((num-1)//3)*3+1
    end = start + 3
    if end > paginator.num_pages:
        end = paginator.num_pages+1
    return paginator.page(num),range(start,end)
def showbook_view(request,num='1'):
    book, page = page_num(num,10)
    if request.method == 'GET':
        return render(request,'showbook.html',{'book':book,'page':page})
    else:
        key = request.POST.get('key')
        if not key:
            return render(request,'showbook.html',{'book':book,'page':page})
        if request.POST.get('method') == 'bookcode':
            book = Bookinfo.objects.filter(bookcode=key,isdelete=0)
        elif request.POST.get('method') == 'bookname':
            book = Bookinfo.objects.filter(bname=key,isdelete=0)
        elif request.POST.get('method') == 'typename':
            book = Bookinfo.objects.filter(btid__typename=key,isdelete=0)
        elif request.POST.get('method') == 'author':
            book = Bookinfo.objects.filter(author=key,isdelete=0)
        elif request.POST.get('method') == 'publishing':
            book = Bookinfo.objects.filter(pubilshing=key,isdelete=0)
        else:
            book = Bookinfo.objects.filter(bcid__bcname=key,isdelete=0)
        return render(request,'showbook.html',{'book':book})


def booktype_view(request):
    if request.method == 'GET':
        booktype = Booktype.objects.all()
        return render(request,'booktype.html',{'booktype':booktype})


def addbooktype_view(request):
    if request.method == 'GET':
        return render(request,'addbooktype.html')
    else:
        typename = request.POST.get('typename')
        btime = request.POST.get('btime')
        booktype = Booktype.objects.create(typename=typename,btime=btime)
        booktype.save()
        return redirect('/book/booktype')


def changebooktype_view(request,num):
    if request.method == 'GET':
        booktype = Booktype.objects.get(btid=num)
        return render(request,'booktypechange.html',{'booktype':booktype})
    else:
        typename = request.POST.get('typename')
        btime = request.POST.get('btime')
        Booktype.objects.filter(btid=num).update(typename=typename,btime=btime)
        return redirect('/book/booktype')


def addbook_view(request):
    if request.method == 'GET':
        booktype = Booktype.objects.all()
        bookcase = Bookcase.objects.all()
        return render(request,'addbook.html',{'booktype':booktype,'bookcase':bookcase})
    else:
        bookcode = request.POST.get('bookcode')
        bname = request.POST.get('bname')
        author = request.POST.get('author')
        booktype = request.POST.get('booktype')
        pubilshing = request.POST.get('pubilshing')
        isbn = request.POST.get('isbn')
        bookcase = request.POST.get('bookcase')
        price = request.POST.get('price')
        booktype = Booktype.objects.get(btid=booktype)
        bookcase = Bookcase.objects.get(bcid=bookcase)
        book = Bookinfo.objects.create(bookcode=bookcode,bname=bname,author=author,btid=booktype,pubilshing=pubilshing,
                                       price=price,isbn=isbn,bcid=bookcase)
        book.save()
        return redirect('/book/')


def changebook_view(request,num):
    if request.method == 'GET':
        booktype = Booktype.objects.all()
        bookcase = Bookcase.objects.all()
        book = Bookinfo.objects.get(bid=num)
        return render(request,'changebook.html',{'book':book,'booktype':booktype,'bookcase':bookcase})
    else:
        bname = request.POST.get('bname')
        author = request.POST.get('author')
        booktype = request.POST.get('booktype')
        pubilshing = request.POST.get('pubilshing')
        isbn = request.POST.get('isbn')
        bookcase = request.POST.get('bookcase')
        price = request.POST.get('price')
        booktype = Booktype.objects.get(btid=booktype)
        bookcase = Bookcase.objects.get(bcid=bookcase)
        Bookinfo.objects.filter(bid=num).update(bname=bname, author=author, btid=booktype,
                                       pubilshing=pubilshing,price=price, isbn=isbn, bcid=bookcase)

        return redirect('/book/')


def booktypedel_view(request,num):
    if request.method == 'GET':
        Booktype.objects.filter(btid=num).delete()
        return redirect('/book/booktype')


def delbook_view(request,num):
    if request.method == 'GET':
        Bookinfo.objects.filter(bid=num).update(isdelete=1)
        return redirect('/book/')


def isbexit_view(request):
    # 接收请求参数
    bookcode = request.GET.get('bookcode','')
    # 判断数据库中是否存在
    bookList = Bookinfo.objects.filter(bookcode=bookcode)
    if bookList:
        return JsonResponse({'flag': True})
    return JsonResponse({'flag': False})


def istype_view(request):
    typename = request.GET.get('typename','')
    typelist = Booktype.objects.filter(typename=typename)
    if typelist:
        return JsonResponse({'flag': True})
    return JsonResponse({'flag': False})