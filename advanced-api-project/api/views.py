from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework 
#List_view for retrieving all books 
class BookListView(generics.ListCreateAPIView):
  """ 
  get: 
  Return a list of all existing books. 
  post: 
  Create a new book instance.
  """
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  filter_backends = [DjangoFilterBackend, SearchFilter]
  filterset_class = BookFilter
  search_fields = ['title', 'author__name'] 
  ordering_fields = ['title', 'publication_year']
  
  
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
  """
   get: Return details of a specific book by ID.
   put: Update an existing book instance. 
   delete: Delete a book instance. 
  """
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthrnticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
	"""
	post: Create a new book instance. 
	"""
queryset = Book.objects.all()
serializer_class = BookSerializer
permission_classes = [IsAuthenticatedOrReadOnly]
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]