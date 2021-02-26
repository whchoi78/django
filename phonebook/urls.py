from django.conf.urls import include, url
from phonebook import views
#127.0.0.1:8000/phonebook

urlpatterns = [
    url(r'^$', views.test),     #그 뒤 더이상 값이 없다면.
    url(r'^index/', views.index,name='index'),
    url(r'^add/', views.add,name='add'),
    url(r'^delete/', views.delete),
    url(r'^detail/([0-9]+)', views.detail,name='detail'),
    url(r'^update/([0-9]+)', views.update,name="update"),
]


