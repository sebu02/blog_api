from django.urls import path

from blog.api.v1.views.blog_views import *

urlpatterns = [
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('create/',BlogCreate.as_view(),name='create'),
    path('list/',BlogListView.as_view(),name='blog-list'),
    path('delete/<int:pk>',BlogDelete.as_view(),name='delete'),
    path('retrieve/<int:pk>',BlogRetrieve.as_view,name='retrieve'),
    
    path('comment/',CommentPost.as_view(),name='comment'),
    path('comment/delete/<int:pk>',CommentDelete.as_view(),name='comment-delete'),
    path('comment/retrieve/<int:id>',CommentRetrieve.as_view(),name='comment-retrieve'),
    path('comment/view/',CommentList.as_view(),name='comment-view'),
    path('search/',BlogSearch.as_view(),name='search'),
    
]
