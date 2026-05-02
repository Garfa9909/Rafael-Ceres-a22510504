from django.shortcuts import render, redirect

from .models import Article
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import user_passes_test, login_required

def es_autor(user):
    return user.groups.filter(name='autores').exists()

def es_el_autor(user, article):
    return article.author == user

def articles_view(request):
    articles = Article.objects.prefetch_related("comments").all()
    context = {'articles': articles, 'es_autor':es_autor(request.user)}
    return render(request, 'articles/articles.html', context)


def article_view(request, id):
    article = Article.objects.prefetch_related("comments").get(id=id)
    context = {'article':article, 'es_el_autor':es_el_autor(request.user, article), 'comment_form':CommentForm()}

    return render(request, 'articles/article.html', context)

@login_required
@user_passes_test(es_autor)
def new_article_view(request):
    form = ArticleForm(request.POST or None, request.FILES)

    if(form.is_valid()):
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        return redirect('articles')

    context = {'form':form}
    return render(request, 'articles/new_article.html', context)

@login_required
@user_passes_test(es_autor)
def edit_article_view(request, id):

    article = Article.objects.get(id=id)
    
    if(request.POST):
        form = ArticleForm(request.POST or None, request.FILES, instance = article)
        if(form.is_valid()):
            form.save()
            return redirect('articles')
    else:
        form = ArticleForm(instance=article)

    context = {'form':form, 'article':article}
    return render(request, "articles/edit_article.html", context)

@login_required
@user_passes_test(es_autor)
def delete_article_view(request, id):

    Article.objects.get(id=id).delete()
    return redirect("articles")

@login_required
def like_article_view(request, id):
    article = Article.objects.get(id=id)

    #If liked, dislike
    if(request.user in article.liked_users.all()):
        article.liked_users.remove(request.user)
        
    else:
        article.liked_users.add(request.user)
        context = {'article':article}
    return redirect("article", id=id)

@login_required
def comment_article_view(request, id):
    article = Article.objects.get(id=id)
    form = CommentForm(request.POST or None, request.FILES)

    if(form.is_valid):
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.save()

        return redirect("article", id=id)

