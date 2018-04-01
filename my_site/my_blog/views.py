from django.views import generic
from .models import Post
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth import views


def index(request):
    return render(request, 'my_blog/index.html')


class ListView(generic.ListView):

    template_name = 'my_blog/list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all()


class DetailView(generic.DetailView):

    model = Post
    template_name = 'my_blog/detail.html'


class CreateView(generic.CreateView):

    model = Post
    template_name = 'my_blog/create.html'
    fields = ['post_title', 'post_content']


class EditView(generic.UpdateView):

    model = Post
    template_name = 'my_blog/edit.html'
    fields = ['post_title', 'post_content']

    def form_valid(self, form):
        form.instance.modified_date = timezone.now()
        return super().form_valid(form)


class DeleteView(generic.DeleteView):

    model = Post
    template_name = 'my_blog/delete.html'
    success_url = reverse_lazy('my_blog:list')


class LoginView(views.LoginView):

    template_name = 'my_blog/login.html'


class LogoutView(views.LogoutView):
    
    template_name = 'my_blog/logout.html'
