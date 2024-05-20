# admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status')
    list_editable = ('status',)  # Allow status to be editable in the list view
   

admin.site.register(Book, BookAdmin)
