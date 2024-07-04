from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Book


class BookListView(ListView):
    model = Book
    paginate_by = 100  # if pagination is desired

