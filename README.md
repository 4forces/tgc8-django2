
## 0.1 Summary of Django App and Model Creation
1. Create app via `django-admin startapp <app_name>`
2. Create template and `template/app` folders in app
3. Create function in `app/view.py` to render the template
4. Create models in `app/models.py`
5. Make migrations and migrate
6. Register the created model in `app/admin.py` to be able to view in django admin

### Notes on "Adding a non-nullable field" Error
#### Lecturer's comments
1. If the field is `IntegerField` use `0`
2. If the field is a string (`CharField`, `TextField`) use `None`
3. If the field is ?? use `??`

#### More from [Django Documentation](https://docs.djangoproject.com/en/3.0/ref/models/fields/#default) on "Null"
1. Avoid using `null` on string-based fields such as `CharField` and `TextField` as this creates 2 possible values for "no data". Use empty string `""` instead.
2. Default is `Null=False`. If `Null=True`, Django will store empty values as NULL in the database

## 0.2 Install new app | Lecturer's Notes: Step 2.1
1. install django: `django-admin startapp books`
2. create superuser:  `python3 manage.py create superuser`


## 1. Create a view function | Lecturer's Notes: Steps 2.3

In `views.py`: create the app: e.g "Books app"
```python
from django.shortcuts import render, HttpResponse
# we import in HttpResponse so that we can use it as the return

# Create your views here.
def index(request):
    return HttpResponse("Books app")
```

## 2. MAP URL TO THE VIEW FUNCTION | Lecturer's Notes: Steps 2.4
In `urls.py`, add the line `path('books/', books.views.index)`
```python
from django.urls import path
import books.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books.views.index)
]
```

## 3. Create the html template | Lecturer's Notes: Steps 4.1 - 4.3
- In `templates` folder, create a folder `books`
- In this folder, create `index.template.html`

## 4. Change the view function to render the template | Lecturer's Notes: Steps 4.4
```python
def index(request):
    return render(request, 'books/index.template.html')
```

## 5. Start app | Lecturer's Notes: Steps 1.4 Test Run
- To start app: In terminal type `python3 manage.py runserver 8080`

## 6. Make Migrations | Lecturer's Notes: Steps 6.0 & 7.2
```
python3 manage.py makemigrations
python3 manage.py migrate
```
- Note 1: To preview migrations to be made: `python3 manage.py makemigrations -–dry-run`
- Note 2: To view all migrated/to be migrated: `python3 manage.py showmigrations`
- Note 3: To view verbose: `python3 manage.py migrate --plan`

## 7. Creating new classes for 'One to Many' (for e.g. 'Genre' or 'Category' for book) | Lecturer's Notes: Step 18

1. In `models.py`, create the class (in this case class = `Genre`):
```python
class Genre(models.Model):
    genre = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.genre
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
- **Remember to import the model at the top of the file**

3. Define this new class relationship in the Book model in `models.py`
```python
class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    # Add this line for Genre class
    # also has models.DELETE, models.RESTRICT(<function>)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

4. Make migrations (may results in error)
- Steps [here](#6-make-migrations--lecturers-notes-steps-60--72)
- Note that if there are already existing values, user will be prompted to fix issue
of addition of 'non-nullable field'. (Ref. Page 23 of Lecturer's Notes). 
- If queried, select option '1' and type 'None' (not a solve-all solution, 
need to be aware of our model relationships when selecting option)

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

5. Allow user to select 'Genre' for Book by adding `'genre'` in the 
`class BookForm()` fields in `forms.py`:
```python
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # add 'genre'
        fields = ('title', 'desc', 'ISBN', 'genre')
```

## 8. Creating new classes for 'Many to Many' (for e.g. 'tags' or 'authors' for 'book') | Lecturer's Notes: Step 20

1. In `models.py`, create the class (in this case class = `Tag`):
```python
class Tag(models.Model):
    tag = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.tag
```

2. Define/Add this new `Tag` class relationship in the Book model in `models.py`
```python
class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    # Add this line for Genre class
    # also has models.DELETE, models.RESTRICT(<function>)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
```

3. Register the `Tag` model in `admin.py`:
```python
# import Genre
from django.contrib import admin
from .models import Book, Genre, Tag

# Register your models here
# register (Genre)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Tag)
```
- **Remember to import the model at the top of the file**

4. Make migrations (M:M does not cause same problem as 1:M/M:1)
- Step [here](#6-make-migrations--lecturers-notes-steps-60--72)

5. Allow user to select 'Tag' for Book by adding `'tag'` in the 
`class BookForm()` fields in `forms.py`:
```python
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'desc', 'ISBN', 'genre', 'tag')
```
---
