from django.contrib import admin
from .models import Tag, Board
# Register your models here.


class TagInline(admin.TabularInline):
    model = Board.tag.through


class BoardAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ('tag',)

admin.site.register(Board, BoardAdmin)
admin.site.register(Tag)

