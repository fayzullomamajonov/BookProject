from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import (
    BookReviewSerializer,
    BooksModelSerializer,
    AuthorModelSerializer,
)
from books.models import ReviewBookModel, BooksModel, AuthorModel
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import viewsets



# Create your views here.


# class BooksAPIView(APIView):
#     def get(self, reques):
#         books = BooksModel.objects.all()
#         serializer = BooksModelSerializer(books, many=True)
#         return Response(data=serializer.data)


# class BooksAPIView(generics.ListCreateAPIView):
#     queryset = BooksModel.objects.all()
#     serializer_class = BooksModelSerializer
#     permission_classes = [IsAuthenticated]

class BooksAPIView(viewsets.ModelViewSet):
    serializer_class = BooksModelSerializer
    queryset = BooksModel.objects.all()
    permission_classes = [IsAuthenticated]



class AuthorAPIView(APIView):
    def get(self, reques):
        authors = AuthorModel.objects.all()
        serializer = AuthorModelSerializer(authors, many=True)
        return Response(data=serializer.data)


class BookReviewAPIView(APIView):
    def get(self, reques):
        books = ReviewBookModel.objects.all()
        serializer = BookReviewSerializer(books, many=True)
        return Response(data=serializer.data)


class BookReviewDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            review = ReviewBookModel.objects.get(id=pk)
        except ReviewBookModel.DoesNotExist:
            return Response(status=404, data={"detail": "Review not found"})

        serializer = BookReviewSerializer(review)
        return Response(data=serializer.data)


class BooksModelDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            book = BooksModel.objects.get(isbn=pk)
        except BooksModel.DoesNotExist:
            return Response(status=404, data={"detail": "Book not found"})

        serializer = BooksModelSerializer(book)
        return Response(data=serializer.data)
