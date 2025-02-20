"""
TO render the html web pages
"""
import random
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string

def home_view(request, *args, **kwargs):

  """
  Take in a request and response a html
  """
  name = "Gaurav"
  random_id = random.randint(1,4)
  # print(args,kwargs)
  #from the database
  article_obj = Article.objects.get(id=random_id)
  article_queryset = Article.objects.all()
  context = {
    "object_list":article_queryset,
    "object":article_obj,
    "title":article_obj.title,
    "id":article_obj.id,
    "content":article_obj.content
  }
  #TEMPLATES
  HTML_STRING = render_to_string("home-view.html",context=context)
  return HttpResponse(HTML_STRING)