from django.urls import path, include
import books.views


urlpatterns = [
    path('home/', books.views.home,
         name='home_route'),
    path('/', books.views.index,
         name='books_route'),
    path('book/update/<book_id>', books.views.update_book,
         name='update_books_route'),
    path('book/delete/<book_id>', books.views.delete_book,
         name='delete_books_route'),
    path('book/create/', books.views.create_book,
         name='create_books_route')
]
