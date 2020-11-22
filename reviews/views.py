from django.shortcuts import render, HttpResponse
from .models import Review
from .forms import ReviewForm
from django.contrib import messages

# Create your views here.


def index(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/index.template.html', {
        'reviews': reviews
    })


def create_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f"New book {form.cleaned_data['title']}"
                             f" has been created")
            return redirect(index)
        else:
            form = ReviewForm()
            return render(request, 'reviews/create_review.template.html', {
                'form':form
            })