# coding=utf-8

from django.conf.urls import url

from sys_settings import views

urlpatterns = [
    url(r'^library_modify/', views.library_modify_view),
    url(r'^manager/', views.manager_view),
    url(r'^manager_add/', views.manager_add_view),
    url(r'^getManagerName/',views.getManagerName_view),
    url(r'^getBookcase/',views.getBookcase_view),
    url(r'^manager_del/(\d+)', views.manager_del_view),
    url(r'^per_settings/(\d+)', views.perset_view),
    url(r'parameter_modify/', views.parameter_modify_view),
    url(r'bookcase/',views.bookcase_view),
    url(r'bookcase_add/',views.bookcase_add_view),
    url(r'bookcase_del/(\d+)',views.bookcase_del_view),
    url(r'bookcase_update/(\d+)',views.bookcase_update_view),
]