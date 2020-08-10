from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorsListView.as_view(), name='author'),
    path('authors/<int:pk>', views.AuthorsDetailView.as_view(), name='author-detail'),
]
