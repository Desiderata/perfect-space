# coding=utf-8
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.forms import ModelForm
from perfect_space.apps.blog.models import Post, Tag


class PostAdminForm(ModelForm):
    class Meta:
        widgets = {
            'title_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'keywords_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'description_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'caption_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'summary_ru': forms.Textarea(attrs={'style': 'width: 500px'}),
            'annotation_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'content_ru': CKEditorUploadingWidget(),

            'title_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'keywords_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'description_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'caption_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'summary_en': forms.Textarea(attrs={'style': 'width: 500px'}),
            'annotation_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'content_en': CKEditorUploadingWidget(),
        }


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('slug', 'date_publication', 'caption_ru', 'description_ru',)
    list_select_related = True
    readonly_fields = ('cover_preview', 'thumb_preview',)
    prepopulated_fields = {'slug': ('title_ru',)}

    fieldsets = [
        (None, {
            'fields': ['date_publication', 'slug', 'cover', 'cover_preview', 'thumb', 'thumb_preview', 'tags']
        }),
        ('Русский', {
            'fields': [
                'title_ru',
                'keywords_ru',
                'description_ru',
                'caption_ru',
                'summary_ru',
                'annotation_ru',
                'content_ru'
            ]}),
        ('Английский', {
            'fields': [
                'title_en',
                'keywords_en',
                'description_en',
                'caption_en',
                'summary_en',
                'annotation_en',
                'content_en'
            ]}),
    ]
admin.site.register(Post, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name_ru',)

    fieldsets = [
        ('Русский', {
            'fields': ['name_ru']}),
        ('Английский', {
            'fields': ['name_en']}),
    ]
admin.site.register(Tag, TagAdmin)
