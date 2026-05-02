from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_view, name="home_articles"),
    path('articles/', views.articles_view, name="articles"),
    path('article/<int:id>', views.article_view, name="article"),
    path('new_article', views.new_article_view, name="new-article"),
    path('edit_article/<int:id>', views.edit_article_view, name="edit-article"),
    path('delete_article/<int:id>', views.delete_article_view, name="delete-article"),
]