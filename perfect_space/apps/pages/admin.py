# coding=utf-8
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from perfect_space.apps.pages.models import Page
from django.contrib import admin
from django.forms import ModelForm


class PageAdminForm(ModelForm):
    class Meta:
        widgets = {
            'title_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'keywords_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'description_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'caption_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'content_ru': CKEditorUploadingWidget(),

            'title_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'keywords_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'description_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'caption_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'content_en': CKEditorUploadingWidget(),
        }


class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm
    list_display = ('slug', 'caption_ru', 'title_ru', 'description_ru',)
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
