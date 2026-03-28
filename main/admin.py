from django.contrib import admin
from .models import Category, Image
from django.utils.safestring import mark_safe


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    can_delete = True
    readonly_fields = ['image_preview']
    fields = ('image', 'image_preview', 'description')

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

admin.site.register(Category, CategoryAdmin)