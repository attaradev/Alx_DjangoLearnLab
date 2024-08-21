from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    return render(request, 'bookshelf/book_list.html')


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request):
    return render(request, 'bookshelf/edit_book.html')
