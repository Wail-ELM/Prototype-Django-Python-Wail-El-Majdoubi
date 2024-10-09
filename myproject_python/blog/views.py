from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Article
from .forms import ArticleForm, CustomUserCreationForm

def all_articles(request):  
    articles = Article.objects.all()
    return render(request, 'blog/all_articles.html', {'articles': articles})

@login_required
def my_articles(request):  
    articles = Article.objects.filter(author=request.user)
    return render(request, 'blog/my_articles.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})

@login_required
def add_article(request):
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
    article = get_object_or_404(Article, pk=article_id)
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
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')  
    return render(request, 'blog/delete_article.html', {'article': article})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})