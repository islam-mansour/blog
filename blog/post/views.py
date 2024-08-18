from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.db.models import Count
from django.db.models import Q

from .forms import CommentForm
from .models import Post


# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        sorted_by = self.request.GET.get('sorted_by')

        # Start with the default queryset
        queryset = Post.objects.all()

        # Filter the posts based on title, content, or author if there's a search query
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(content__icontains=search_query) |
                Q(author__username__icontains=search_query) |
                Q(author__first_name__icontains=search_query) |
                Q(author__last_name__icontains=search_query)
            )

        # Set the post order
        ordering = ['-created_at', '-views']
        if sorted_by == 'views':
            ordering = ['-views']
        elif sorted_by == 'likes':
            queryset = queryset.annotate(likes_count=Count('like')).order_by('-likes_count', '-views')

        # Apply the final ordering to the queryset
        if not sorted_by == 'likes':
            queryset = queryset.order_by(*ordering)
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # Get the post object
        post = self.get_object()

        # Increment the views count by 1
        post.views += 1
        post.save()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_object().title
        context['comment_form'] = CommentForm()
        return context


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'form.html'
    fields = ['title', 'content', 'media']
    success_message = 'The post was successfully posted.'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Make Post'
        context['form_title'] = 'Make Post'
        context['form_btn'] = 'Post'
        context['with_media'] = True
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'form.html'
    fields = ['title', 'content', 'media']
    success_message = 'The post was successfully updated.'

    def test_func(self):
        # Check if the authenticated user is the author of the post
        return self.get_object().author == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Post'
        context['form_title'] = 'Update Post'
        context['form_btn'] = 'Update'
        context['with_media'] = True
        return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')  # Redirect to the home page after deletion
    context_object_name = 'post'
    success_message = 'The post was successfully deleted.'
    
    def test_func(self):
        # Check if the authenticated user is the author of the post
        return self.get_object().author == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Post'
        return context