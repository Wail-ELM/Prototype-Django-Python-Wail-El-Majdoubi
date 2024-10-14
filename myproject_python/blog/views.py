from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Article
from .forms import ArticleForm, UserSignupForm

def all_articles(request):
    """
    Display all articles.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered template with all articles.
    """
    articles = Article.objects.all()
    return render(request, 'blog/all_articles.html', {'articles': articles})

@login_required
def my_articles(request):
    """
    Display articles written by the logged-in user.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered template with user's articles.
    """
    articles = Article.objects.filter(author=request.user)
    return render(request, 'blog/my_articles.html', {'articles': articles})

def article_detail(request, article_id):
    """
    Display details of a specific article.

    Args:
        request: The HTTP request object.
        article_id: The ID of the article to display.

    Returns:
        Rendered template with article details.
    """
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})

@login_required
def add_article(request):
    """
    Create a new article.

    Args:
        request: The HTTP request object.

    Returns:
        Form for adding an article or redirects to article detail on success.
    """
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = ArticleForm()
    return render(request, 'blog/add_article.html', {'form': form})

@login_required
def edit_article(request, article_id):
    """
    Edit an existing article.

    Args:
        request: The HTTP request object.
        article_id: The ID of the article to edit.

    Returns:
        Form for editing an article or redirects to article detail on success.
    """
    article = get_object_or_404(Article, pk=article_id)
    if request.user != article.author:
        return redirect('article_detail', article_id=article.id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/edit_article.html', {'form': form, 'article': article})

@login_required
def delete_article(request, article_id):
    """
    Delete an existing article.

    Args:
        request: The HTTP request object.
        article_id: The ID of the article to delete.

    Returns:
        Confirmation page for deleting an article or redirects to all articles on success.
    """
    article = get_object_or_404(Article, pk=article_id)
    if request.user != article.author:
        return redirect('article_detail', article_id=article.id)
    if request.method == 'POST':
        article.delete()
        return redirect('all_articles')
    return render(request, 'blog/delete_article.html', {'article': article})


class CustomLoginView(SuccessMessageMixin, LoginView):
    """
    Custom login view to display a success message upon successful login.
    """
    template_name = 'registration/login.html'
    success_message = "You were successfully logged in."

class CustomSignupView(CreateView):
    """
    Custom signup view to handle user registration.
    """
    form_class = UserSignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')