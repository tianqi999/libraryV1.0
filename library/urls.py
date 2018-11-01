#coding=utf-8
from django.conf.urls import url

from library import views

urlpatterns = [
    url(r'^login/',views.login_view),
    url(r'^main/', views.main_view),
    url(r'^borrowQuery/', views.borrowQuery_view),
    url(r'^bremind/', views.bremind_view),
    url(r'^pwd_Modify/', views.pwd_Modify_view),
    url(r'^bookBorrow/',views.bookBorrow_view),
]