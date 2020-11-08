from django.db import models

# Create your models here.

# we want to have a Book table inside our database


class Book(models.Model):
    # what are the fields (aka attributes) of this table

    # eqv. title VARCHAR(255) NOT NULL
    title = models.CharField(blank=False, max_length=255)

    # eqv. ISBN VARCHAR(255) NOT NULL
    ISBN = models.CharField(blank=False, max_length=255)

    # eqv. desc TEXT NOT NULL
    desc = models.TextField(blank=False)

 # toString function -- it allows us to state the string representation
    # of a class
    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    date_of_birth = models.DateTimeField(blank=False)
    dob = models.DateField(blank=False)


def __str__(self):
    return self.first_name + " " + self.last_name


class Author2(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    dob = models.DateField(blank=False)


def __str__(self):
    return self.first_name + " " + self.last_name
