from django.urls import path
from todo.views import (

    all_todos_view,
    category_view,
    todo_view,
    tag_view,
)
app_name='todo'

urlpatterns = [
    #all todos
    path('', all_todos_view, name='all_todos_view'),

    path('category/<slug:category_slug>/',category_view, name='category_view'),
    path('todo/<slug:todo_slug>/',todo_view, name='todo_view'),
    #todo detail
    path('category/<slug:category_slug>/todo/<int:id>/', todo_view, name='todo_view'),
]