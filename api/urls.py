from django.urls import path
from .views import BookReviewAPIView,AuthorAPIView,BooksAPIView,BookReviewDetailAPIView,BooksModelDetailAPIView


urlpatterns = [
    path('reviews/',BookReviewAPIView.as_view(),name='reviews-api'),
    path('books/',BooksAPIView.as_view(),name='books-api'),
    path('author/',AuthorAPIView.as_view(),name='authors-api'),
    path('review/<int:pk>/',BookReviewDetailAPIView.as_view(),name='review-api'),
    path('book/<int:pk>/',BooksModelDetailAPIView.as_view(),name='book-api'),
]