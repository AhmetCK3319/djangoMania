from django.contrib import admin
from .models import Todo,TodoCategory,TodoTag


# Register your models here.

#database oluşturulan kolonların özelliklerini gösterme
class TodoTagAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'pk',
        'is_active',
    ]


class TodoCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'pk',
        'is_active',
        
    ]

class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'pk',
        'is_active',
        'created_at',
        'updated_at',
    ]
    list_display_links =[
        'pk',
        'category',
        'title',
    ]

admin.site.register(Todo,TodoAdmin)
admin.site.register(TodoCategory,TodoCategoryAdmin)
admin.site.register(TodoTag,TodoTagAdmin)