from django.conf.urls import include, url
from django.contrib import admin
from mainApp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mainApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(test)/', views.test),
    url(r'^phonebook/', include("phonebook.urls",namespace="PB")),
    #http://127.0.0.1:8000/phonebook, namespace는 서브앱으로 이동할때 사용
]
