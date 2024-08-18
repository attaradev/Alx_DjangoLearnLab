from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Book, Library


def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'books'


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.book_set.all()
        return context
