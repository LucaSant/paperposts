from django.urls import path
from .  import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>/", views.post_details, name='post_details'),
    path('create_post', views.create_post, name='create_post'),
]