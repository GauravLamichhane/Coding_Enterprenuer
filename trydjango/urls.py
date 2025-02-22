from django.contrib import admin
from django.urls import path, re_path


from . views import home_view
from articles.views import (
article_search_view,
article_create_view,
article_detail_view
)
from accounts.views import login_view,logout_view
urlpatterns = [
    path("",home_view),
    path("login/",login_view),
    path("logout/",logout_view),
    path("articles/",article_search_view),
    path("articles/create/",article_create_view),
    path("articles/<int:id>/",article_detail_view),
    path("admin/", admin.site.urls),
]