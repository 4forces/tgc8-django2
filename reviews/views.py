from django.shortcuts import render, HttpResponse
from .models import Review
from .forms import ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/index.template.html', {
        'reviews': reviews
    })

@login_required
def create_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            # save the form it will the create model instance
            # i.e it will insert the new row into the table in the database	            
            # when we specify Commit=False, means don't save to database directly
            review = form.save(commit=False)
            review.user = request.user  # request.user will contain the currently logged in user
            review.save()            
            messages.success(request,
                             f"New book {form.cleaned_data['title']}"
                             f" has been created")
            return redirect(index)
        else:
            form = ReviewForm()
            return render(request, 'reviews/create_review.template.html', {
                'form':form
            })