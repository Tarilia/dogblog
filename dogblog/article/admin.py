from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Article, Category, Tags

admin.site.register(Article)


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'id', 'title', 'slug')
    list_display_links = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Основная информация', {'fields': ('title', 'slug', 'parent')}),
        ('Описание', {'fields': ('description',)})
    )


@admin.register(Tags)
class TagPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')
    list_display_links = ('id', 'tag')
