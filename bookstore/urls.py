from django.conf.urls import url
from django.contrib import admin
from .core import views as v

urlpatterns = [
    url(r'^$', v.home, name='home'),
    url(r'^adduser/$', v.adduser, name='adduser'),
    url(r'^customers/$', v.customer_list, name='customer_list'),
    # url(r'^customers/$', v.SomeProtectedView.as_view(), name='customer_list'),
    url(r'^books/$', v.BookList.as_view(), name='book_list'),
    url(r'^stores/$', v.StoreList.as_view(), name='store_list'),
    url(r'^stores/(?P<pk>\d+)/$', v.StoreDetail.as_view(), name='store_detail'),
    url(r'^admin/', admin.site.urls),
]
