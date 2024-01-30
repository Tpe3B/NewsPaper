from django.contrib import admin
from .models import Category, Post, Author, PostCategory

# создаём новый класс для представления товаров в админке

# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)

