#coding=utf-8

from django.conf.urls import url

from book_operation import views

urlpatterns = [
    url(r'^bookBorrow/',views.bookBorrow_view),
    url(r'^getReaderInfo/',views.getReaderInfo),
    url(r'^getBookInfo/', views.getBookInfo),
]