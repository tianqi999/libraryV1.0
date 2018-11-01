from django.conf.urls import url
from reader import views
urlpatterns = [
    url(r'^$',views.readerset_view),
    url(r'^page/(\d+)',views.readerset_view),
    url(r'^readertype/',views.readertype_view),
    url(r'^addreader/',views.addreader_view),
    url(r'^readerchange/(\d+)',views.readerchange_view),
    url(r'^readerdel/(\d+)',views.readerdel_view),
    url(r'^show/(\d+)',views.show_view),
    url(r'^isExist/$',views.exist_View),
]
