from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Todo,TodoCategory,TodoTag

@login_required(login_url = '/admin/login/' )
def all_todos_view(request):
    # todos=Todo.objects.all()
    todos = Todo.objects.filter(
        user = request.user,
        is_active=True,
        
        )
    context=dict(
        todos=todos,
    )
    return render(request, 'todo/todo_list.html',context )

# def todo_detail(request,id):
#     try:    
#         todo=Todo.objects.get(pk=id)
#         context=dict(
#             todo=todo,
#         )
#         return render(request,'todo/todo_detail.html',context)
#     except Todo.DoesNotExist:
#         raise Http404  

@login_required(login_url = '/admin/login/' )
def category_view(request,category_slug):
    category = get_object_or_404(TodoCategory, slug=category_slug)
    todos = Todo.objects.filter(
        user = request.user,
        is_active=True,
        category=category,
        )
    context=dict(
        category=category,
        todos=todos,
    )
    return render (request,'todo/todo_list.html',context)


@login_required(login_url = '/admin/login/' )
def todo_view(request,category_slug,id): 

    todo=get_object_or_404(Todo, category__slug = category_slug, pk = id, user = request.user)

    context=dict(
        todo=todo,
        )
    return render(request,'todo/todo_detail.html',context)

@login_required(login_url='/admin/login/')
def tag_view(request, tag_slug):
    tag = get_object_or_404 (TodoTag, slug = tag_slug )
    context = dict(
        tag=tag,
        todos=tag.todo_set.all(user=request.user),
    )
    return render(request, 'todo/todo_list.html', context)