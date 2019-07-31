from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Tag

class PostList(ListView):
    model = Post
    paginate_by = 5

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'music']

    def dispatch(self, *args, **kwargs):
        return super(PostCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.writer = self.request.user
        obj.save()
        Post.tag_save(obj)
        obj.save()
        return redirect('/board/read/'+str(obj.id))

class PostRead(DetailView):
    model = Post

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content', 'music']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.writer = self.request.user
        Post.tag_save(obj)
        obj.save()
        return redirect('/board/read/'+str(obj.id))

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('list')

def tagedList(request, tag=None):

    if tag:
        post_list = Post.objects.filter(tag_set__name__iexact=tag)
    else:
        post_list = Post.object.all()

    paginator = Paginator(post_list,3)
    page_num = request.POST.get('page')

    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'board/post_list.html', {
        'tag': tag,
        'object_list': posts,
    })