from django.urls import path

from .views import BookListView

urlpatterns = [
    path("", BookListView.as_view(template_name="books/book_list.html"), name="book-list"),
    path("<str:ordring>")
]