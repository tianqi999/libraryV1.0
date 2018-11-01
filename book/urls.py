from django.conf.urls import url
from book import views

urlpatterns = [
    url(r'^$',views.showbook_view),
    url(r'^showbook/(\d+)',views.showbook_view),
    url(r'^booktype/',views.booktype_view),
    url(r'^addbooktype',views.addbooktype_view),
    url(r'^changebooktype/(\d+)',views.changebooktype_view),
    url(r'^booktypedel/(\d+)',views.booktypedel_view),
    url(r'^addbook/',views.addbook_view),
    url(r'^changebook/(\d+)',views.changebook_view),
    url(r'^delbook/(\d+)',views.delbook_view),
    url(r'^isbExist/$',views.isbexit_view),
    url(r'^istype/$',views.istype_view),
]