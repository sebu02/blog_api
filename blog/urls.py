from django.urls import path

from blog.api.v1.views.blog_views import *

urlpatterns = [
    path('login/',Register.as_view(),name='register')
]
