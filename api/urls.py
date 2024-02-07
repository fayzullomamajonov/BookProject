# from django.urls import path
# from .views import BookReviewAPIView,AuthorAPIView,BooksAPIView,BookReviewDetailAPIView,BooksModelDetailAPIView


# urlpatterns = [
#     path('reviews/',BookReviewAPIView.as_view(),name='reviews-api'),
#     path('books/',BooksAPIView.as_view(),name='books-api'),
#     path('author/',AuthorAPIView.as_view(),name='authors-api'),
#     path('review/<int:pk>/',BookReviewDetailAPIView.as_view(),name='review-api'),
#     path('book/<int:pk>/',BooksModelDetailAPIView.as_view(),name='book-api'),
# ]

# ******************************************************

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BooksAPIView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', BooksAPIView)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]