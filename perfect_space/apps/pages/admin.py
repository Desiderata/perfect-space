# coding=utf-8
from ckeditor.widgets import CKEditorWidget
from perfect_space.apps.pages.models import Page
from django.contrib import admin
from django.forms import ModelForm


class PageAdminForm(ModelForm):
    class Meta:
        widgets = {
            'content_ru': CKEditorWidget(),
            'content_en': CKEditorWidget(),
        }


class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm
    list_display = ('caption_ru', 'title_ru', 'description_ru', 'slug')
    list_select_related = True
    prepopulated_fields = {'slug': ('title_ru',)}

    fieldsets = [
        (None, {
            'fields': ['slug', 'template']
        }),
        ('Русский', {
            'fields': ['title_ru', 'keywords_ru', 'description_ru', 'caption_ru', 'content_ru']}),
        ('Английский', {
            'fields': ['title_en', 'keywords_en', 'description_en', 'caption_en', 'content_en']}),
    ]
admin.site.register(Page, PageAdmin)
