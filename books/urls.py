from django.urls import path, include
import books.views

urlpatterns = [
    path('', books.views.index,
         name='books_route'),
    path('search/', books.views.search),
    path('create', books.views.create_book,
         name='create_books_route'),       
    path('update/<book_id>', books.views.update_book,
         name='update_books_route'),
    path('delete/<book_id>', books.views.delete_book,
         name='delete_books_route'),
     path('details/<book_id>', books.views.view_book_details, name="book_details_route"),
]
