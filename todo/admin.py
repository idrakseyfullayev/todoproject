from django.contrib import admin

# Register your models here.

from todo.models import TodoModel

@admin.register(TodoModel)
class TodoAdmin(admin.ModelAdmin):
    pass
