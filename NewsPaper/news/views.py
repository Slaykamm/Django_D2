# from django.shortcuts import render
from django.views.generic import ListView, DetailView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Post, Author, Category, PostCategory, Comment, User
from datetime import datetime
 
 
class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через html-шаблон
    queryset = Post.objects.order_by('-post_datetime')  #сортируем по уменьшению

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        
        return context

class PostDetail(DetailView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'new.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'post'   # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через html-шаблон



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        
        return context  