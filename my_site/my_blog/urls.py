from django.urls import path, re_path
from . import views

app_name = 'my_blog'
urlpatterns = [
    path('list/', views.ListView.as_view(), name='list'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
    re_path(r'^.*$', views.index, name='index')
]
