# coding=utf-8
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.forms import ModelForm

from perfect_space.apps.interiors.models import Interior


class InteriorAdminForm(ModelForm):
    class Meta:
        widgets = {
            'title_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'keywords_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'description_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'caption_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'idea_ru': CKEditorUploadingWidget(),
            'content_ru': CKEditorUploadingWidget(),

            'title_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'keywords_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'description_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'caption_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'idea_en': CKEditorUploadingWidget(),
            'content_en': CKEditorUploadingWidget(),
        }


class InteriorAdmin(admin.ModelAdmin):
    form = InteriorAdminForm
    list_display = ('caption_ru', 'slug', 'date_publication', 'description_ru',)
    list_select_related = True
    readonly_fields = ('cover_preview', 'thumb_preview',)
    prepopulated_fields = {'slug': ('title_ru',)}

    fieldsets = [
        (None, {
            'fields': ['date_publication', 'slug', 'square', 'ceil', 'bedrooms', 'cover', 'cover_preview', 'thumb', 'thumb_preview']
        }),
        ('Русский', {
            'fields': [
                'title_ru',
                'keywords_ru',
                'description_ru',
                'caption_ru',
                'idea_ru',
                'content_ru'
            ]}),
        ('Английский', {
            'fields': [
                'title_en',
                'keywords_en',
                'description_en',
                'caption_en',
                'idea_en',
                'content_en'
            ]}),
    ]
admin.site.register(Interior, InteriorAdmin)
