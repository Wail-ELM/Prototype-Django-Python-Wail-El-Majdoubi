from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.my_articles, name='my_articles'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('add/', views.add_article, name='add_article'),
    path('article/<int:article_id>/edit/', views.edit_article, name='edit_article'),
    path('article/<int:article_id>/delete/', views.delete_article, name='delete_article'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('all_articles/', views.all_articles, name='all_articles'), 
    path('my_articles/', views.my_articles, name='my_articles'), 
    # path('manage_articles/', views.manage_articles, name='manage_articles'),
]