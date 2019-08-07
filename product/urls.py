from django.urls import path
from . import views

urlpatterns = [
    # Create
    path('new/', views.new),
    path('create/', views.create),
    
    # Read
    path('', views.index),
    path('<int:nono_id>/', views.detail),

    # Delete
    path('<int:nono_id>/delete/', views.delete),

    # Update
    path('<int:nono_id>/edit/', views.edit),
    path('<int:nono_id>/update/', views.update),
]
