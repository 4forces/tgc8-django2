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
    path('authors/', books.views.authors,
         name='authors_route'),
    path('authors/create/', books.views.create_author,
         name='create_authors_route'),
    path('authors/edit/<author_id>', books.views.edit_author,
         name='edit_authors_route'),
    path('authors/delete/<author_id>', books.views.delete_author,
         name='delete_authors_route'),
    path('books/', include('books.urls')),
    path('reviews/', include('reviews.urls')),
    path('carts/', include('cart.urls')),
    path('checkout/', include('checkout.urls'))

]
