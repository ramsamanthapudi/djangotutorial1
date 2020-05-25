from django.urls import path, re_path
from . import views

urlpatterns = [
    path('cbvget/', views.classbasedview.as_view()),  # we have to give .as_view() function when we are using class based view
    path('tmplt/', views.Templatebasedclassview.as_view()),
    path('list/', views.Listbasedview.as_view(), name='list'),
    path('detail/<int:pk>/', views.Detailbaseview.as_view(), name='detail'),
    path('create/', views.Employeecreateview.as_view()),
    re_path(r'^update/(?P<pk>\d+)/$', views.Employeeupdateview.as_view(), name='update'),
    re_path(r'^delete/(?P<pk>\d+)/$', views.Employeedeleteview.as_view(), name='delete')
]