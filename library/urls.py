from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path("library/", BookListView.as_view(), name="library"),
    path("book_detail/<int:id>/", BookDetailView.as_view(), name="book-detail"),
]