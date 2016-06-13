# coding=utf-8
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.forms import ModelForm
from perfect_space.apps.projects.models import Project


class ProjectAdminForm(ModelForm):
    class Meta:
        widgets = {
            'title_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'keywords_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'description_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'caption_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'authors_ru': CKEditorUploadingWidget(),
            'address_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'date_constructed_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'date_planning_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'date_realization_ru': forms.TextInput(attrs={'style': 'width: 500px'}),
            'idea_ru': CKEditorUploadingWidget(),
            'content_ru': CKEditorUploadingWidget(),

            'title_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'keywords_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'description_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'caption_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'authors_en': CKEditorUploadingWidget(),
            'address_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'date_constructed_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'date_planning_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'date_realization_en': forms.TextInput(attrs={'style': 'width: 500px'}),
            'idea_en': CKEditorUploadingWidget(),
            'content_en': CKEditorUploadingWidget(),
        }


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ('slug', 'caption_ru', 'description_ru',)
    list_select_related = True
    readonly_fields = ('cover_preview', 'thumb_preview',)
    prepopulated_fields = {'slug': ('title_ru',)}

    fieldsets = [
        (None, {
            'fields': ['slug', 'cover', 'cover_preview', 'thumb', 'thumb_preview']
        }),
        ('Русский', {
            'fields': [
                'title_ru',
                'keywords_ru',
                'description_ru',
                'caption_ru',
                'authors_ru',
                'address_ru',
                'date_constructed_ru',
                'date_planning_ru',
                'date_realization_ru',
                'idea_ru',
                'content_ru'
            ]}),
        ('Английский', {
            'fields': [
                'title_en',
                'keywords_en',
                'description_en',
                'caption_en',
                'authors_en',
                'address_en',
                'date_constructed_en',
                'date_planning_en',
                'date_realization_en',
                'idea_en',
                'content_en'
            ]}),
    ]
admin.site.register(Project, ProjectAdmin)
