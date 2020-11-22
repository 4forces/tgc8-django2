from django import forms
from .models import Review


# define new class 'BookForm'
class ReviewForm(forms.ModelForm):
    # meta class to define which model the form is for
    class Meta:
        # define model as 'Book'
        model = Review
        fields = ('__all__')