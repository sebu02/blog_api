from django.urls import path

from blog.api.v1.views.blog_views import *

urlpatterns = [
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('create/',BlogCUD.as_view(),name='create'),
    path('update/<int:pk>',BlogCUD.as_view(),name='update'),
    path('delete/<int:pk>',BlogCUD.as_view(),name='delete'),
    path('list/',BlogListView.as_view(),name='blog-list'),
    path('retrieve/<int:pk>',BlogRetrieve.as_view,name='retrieve'),
    
    path('comment/',CommentCUD.as_view(),name='comment'),
    path('comment/delete/<int:pk>',CommentCUD.as_view(),name='comment-delete'),
    path('comment/update/<int:id>/',CommentCUD.as_view,name='comment-update'),
    path('comment/retrieve/<int:id>',CommentRetrieve.as_view(),name='comment-retrieve'),
    path('comment/view/<int:id>',CommentList.as_view(),name='comment-view'),
    path('search/',BlogSearch.as_view(),name='search'),
    
    path('comment/reply/',CommentReply.as_view(),name='comment-reply'),
    path('comment/reply/update/<int:id>',CommentReply.as_view(),name='comment-update'),
    path('comment/reply/delete/<int:id>',CommentReply.as_view,name='comment-delete'),
]
