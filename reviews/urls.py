from django.urls import path, include
import reviews.views


urlpatterns = [
    path('review/', reviews.views.index,
         name='reviews_route'),
    path('review/create', reviews.views.create_review),
]
