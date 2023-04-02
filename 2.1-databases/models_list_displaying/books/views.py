from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book

CONTENT = Book.objects.order_by('pub_date')

def books_view(request, pub_date=None):

    if pub_date is None:
        template = 'books/books_list.html'

        context = {
            'books': CONTENT,

        }
    else:
        template = 'books/pub_date_book.html'
        page_number = int(request.GET.get('page', 1))
        pagi = Paginator(CONTENT, 1)
        for number in range(1, pagi.count + 1):
            page = pagi.get_page(number)
            if pub_date == str(page.object_list[0].pub_date):
                page_number = number

        page = pagi.get_page(page_number)
        if page.has_previous:
            prev_page = page_number - 1

        if page.has_next:
            next_page = page_number + 1
        context = {
            'page': page,
            'next': str(pagi.get_page(next_page).object_list[0].pub_date),
            'prev': str(pagi.get_page(prev_page).object_list[0].pub_date),

        }

    return render(request, template, context)
