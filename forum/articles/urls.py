from django.urls import path, include
from articles import views

urlpatterns = [
    path('archive/', views.archive, name='archive'),
    path('', views.forum, name='forum'),
    path('article_new/', views.create_post, name='create_post'),
    path('article/<article_id>/', views.get_article, name='get_article'),

    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.archive, name='archive'),
    path('accounts/profile/', views.archive, name='archive'),
    ]
