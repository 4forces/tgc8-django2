"""BookReviewsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import books.views
import reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('home/', books.views.home,
         name='home_route'),
    path('books/', books.views.index,
         name='books_route'),
    path('reviews/', reviews.views.index,
         name='reviews_route'),
    path('authors/', books.views.authors,
         name='authors_route'),
    path('create_books/', books.views.create_book,
         name='create_books_route'),
    path('create_authors/', books.views.create_author,
         name='create_authors_route'),
    path('update_books/<book_id>', books.views.update_book,
         name='update_books_route'),
    path('edit_authors/<author_id>', books.views.edit_author,
         name='edit_authors_route'),
    path('delete_authors/<author_id>', books.views.delete_author,
         name='delete_authors_route'),
    path('delete_books/<book_id>', books.views.delete_book,
         name='delete_books_route')
]
