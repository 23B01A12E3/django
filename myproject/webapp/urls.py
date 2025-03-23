from django.urls import path
from . import views
urlpatterns=[
    path('',views.homepages,name='home'),
    path('first/',views.firstweb,name='first'),
    path('second/',views.secondweb,name='second'),
    path('html/',views.htmlpage,name='html'),
]