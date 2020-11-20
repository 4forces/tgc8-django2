## 0. Install new app
`django-admin startapp books`

## 1. Create a view function

In `views.py`: create the app: e.g "Books app"
```python
from django.shortcuts import render, HttpResponse
# we import in HttpResponse so that we can use it as the return

# Create your views here.
def index(request):
    return HttpResponse("Books app")
```

## 2. MAP URL TO THE VIEW FUNCTION
In `urls.py`, add the line `path('books/', books.views.index)`
```python
from django.urls import path
import books.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books.views.index)
]
```

## 3. Create the html template
- In `templates` folder, create a folder `books`
- In this folder, create `index.template.html`

## 4. Change the view function to render the template
```python
def index(request):
    return render(request, 'books/index.template.html')
```

## 5. Start app
- To start app: In terminal type `python3 manage.py runserver 8080`

## 6. Make Migrations 
```
python3 manage.py makemigrations
python3 manage.py migrate
```

## 7. Creating new classes

1. In `models.py`, create the class (in this case class = `Genre`):
```python
class Genre(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title
```

2. Register the model in `admin.py`:
```python
# import Genre
from django.contrib import admin
from .models import Book, Genre

# Register your models here
# register (Genre)
admin.site.register(Book)
admin.site.register(Genre)
```

3. Define this new class relationship in the Book model in `models.py`
```python
class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    # Add this line for Genre class:
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

4. Make migrations (results in error)
- Note that if there are already existing values, user will be prompted to fix issue
of addition of 'non-nullable field'. (Ref. Page 23 of Lecturer's notes)

5. After Step 4, we need to go to `models.py` and comment out the `genre= ` line or the server will crash.
```python
class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    # Add this line for Genre class:
    # genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```
   - Make migrations again to update the server after commenting out the `genre= ` line

5. Allow user to select 'Genre' for Book by adding `'genre'` in the `class BookForm()` fields:
```python
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # add 'genre'
        fields = ('title', 'desc', 'ISBN', 'genre')
```


---
