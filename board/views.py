from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

class PostList(ListView):
    model = Post
    paginate_by = 10

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'music']

    def dispatch(self, *args, **kwargs):
        return super(PostCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.writer = self.request.user
        obj.save()
        return redirect('/board/read/'+str(obj.id))

class PostRead(DetailView):
    model = Post

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content', 'music']
    success_url = reverse_lazy('read')

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('list')