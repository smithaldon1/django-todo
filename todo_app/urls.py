from django.urls import path
from .views import (
    todo_create,  
    todo_list, 
    todo_detail, 
    todo_update,
    todo_delete,
)

urlpatterns = [
    path('', todo_list),
    path('create/', todo_create),
    path('<id>/', todo_detail),
    path('<id>/update', todo_update),
    path('<id>/delete', todo_delete)
]