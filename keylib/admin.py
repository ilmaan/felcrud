from django.contrib import admin 

from .models import Library, Hero, Employee

# Register your models here.

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['id','bname','bauthor','bquantity']

# MEDIUM -STACK OVERFLOW CRUD
admin.site.register(Hero)



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','city']