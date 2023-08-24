from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


# Create your views here.
class NewsList(ListView):
    model = Post
    date = 'dateCreation'
    post_author = 'author'
    post_title = 'title'
    post_text = 'text'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

class NewsDetail(DetailView):
    model = Post
    template_name = 'item.html'
    context_object_name = 'item'