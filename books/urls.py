from django.urls import path
from .api import BookViewSet, CommentsViewSet
from .views import NewBookView, BookDetailView, BookUpdateView, BookDeleteView, NewCommentView, UpdateCommentView

urlpatterns = [
    path('new/', NewBookView.as_view(), name='new-book'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
    path('new/comment/<int:pk>', NewCommentView.as_view(), name='book-comment'),
    path('update/comment/<int:pk>', UpdateCommentView.as_view(),
         name='book-comment-update'),
    path('delete/comment/<int:pk>', UpdateCommentView.as_view(),
         name='book-comment-delete'),
    path('', BookViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='book-list'),
    path('book-detail/<int:pk>', BookViewSet.as_view({
        'get': 'retrieve',
    }), name='book-detailset'),
    path('update/detail/<int:pk>/', BookViewSet.as_view({
        'get': 'retrieve2',
        'post': 'update'
    }), name='book-detailupdateinfo'),
    path('book-delete/<int:pk>/', BookViewSet.as_view({
        'get': 'retrieve3',
        'post': 'destroy'
    }), name='book-deletepage'),
    path('new-comment/<int:pk>/', CommentsViewSet.as_view({
        'get': 'retrieve',
        'post': 'create'
    }), name='book-new-comment'),
    path('update-comment/<int:pk>/', CommentsViewSet.as_view({
        'get': 'retrieve',
        'post': 'update'
    }), name='book-update-comment'),
    path('delete-comment/<int:pk>/', CommentsViewSet.as_view({
        'post': 'destroy'
    }), name='book-destroy-comment'),





]
