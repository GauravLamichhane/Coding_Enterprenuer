from django.shortcuts import render
from articles.models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm


def article_search_view(request):

  query_dict = request.GET#This is a dictionary
  query = query_dict.get("q")#<input type="text" name="q">

  try:
    query = int(query_dict.get("q"))
  except:
    query = None
  article_obj = None
  if query is not None:
    article_obj = Article.objects.get(id=query)
  context = {
    "object":article_obj
  }
  return render(request,"articles/search.html",context = context)


@login_required
def article_create_view(request):
  form = ArticleForm(request.POST or None)
  # print(dir(form))
  context ={
    "form":form
  }
  if form.is_valid():
      article_object = form.save()
      context['form'] = ArticleForm()
      # context["object"] = article_object 
      # context["created"] = True
  return render(request, "articles/create.html",context=context)


def article_detail_view(request,id=None):
  article_obj = None
  if id is not None:
    article_obj = Article.objects.get(id=id)
  context ={
    "object":article_obj,
  }
  return render(request,"articles/detail.html",context=context)