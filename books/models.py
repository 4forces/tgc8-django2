from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.genre

class Category(models.Model):
    category = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.tag


class Author2(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    dob = models.DateField(blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name


# we want to have a Book table inside our database
class Book(models.Model):
    # what are the fields (aka attributes) of this table
    # eqv. title VARCHAR(255) NOT NULL
    title = models.CharField(blank=False, max_length=255)
    # eqv. ISBN VARCHAR(255) NOT NULL
    ISBN = models.CharField(blank=False, max_length=255)
    # eqv. desc TEXT NOT NULL
    desc = models.TextField(blank=False)
    # toString function -- it allows us to state the
    # string representation of a class
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    author = models.ManyToManyField(Author2)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return self.title


# # Commented out. Replaced by 'Author2'
# class Author(models.Model):
#     first_name = models.CharField(blank=False, max_length=255)
#     last_name = models.CharField(blank=False, max_length=255)
#     date_of_birth = models.DateTimeField(blank=False)
#     dob = models.DateField(blank=False)

#     def __str__(self):
#         return self.first_name + " " + self.last_name
