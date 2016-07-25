# coding=utf-8
from django.contrib import admin
from perfect_space.apps.publications.models import Publication, PublicationImage


class PublicationImageInline(admin.StackedInline):
    readonly_fields = ('image_preview',)
    model = PublicationImage
    min_num = 1
    extra = 0


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'description_ru',)
    readonly_fields = ('cover_preview',)
    inlines = (PublicationImageInline,)

    fieldsets = [
        (None, {
            'fields': ['date', 'cover', 'cover_preview']
        }),
        ('Русский', {
            'fields': ['title_ru', 'description_ru']}),
        ('Английский', {
            'fields': ['title_en', 'description_en']}),
    ]
admin.site.register(Publication, PublicationAdmin)
