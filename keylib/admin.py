from django.contrib import admin

from .models import Library

# Register your models here.

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['id','bname','bauthor','bquantity']