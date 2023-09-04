from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
from .filters import PostFilter


# Create your views here.
class NewsList(ListView):
    model = Post
    date = 'dateCreation'
    post_author = 'author'
    post_title = 'title'
    post_text = 'text'
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-dateCreation']
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwards):
        context = super().get_context_data(**kwards)
        context['filterset'] = self.filterset
        return context




class NewsDetail(DetailView):
    model = Post
    template_name = 'item.html'
    context_object_name = 'item'
    name = 'post_detail'