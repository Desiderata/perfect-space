# coding=utf-8
"""perfect_space URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from perfect_space.apps.blog.views import BlogList, BlogDetail
from perfect_space.apps.interiors.views import InteriorDetail, InteriorList
from perfect_space.apps.pages.views import PageView
from perfect_space.apps.projects.views import ProjectDetail, ProjectList

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]

urlpatterns += i18n_patterns(
    url(r'^project/(?P<slug>[a-z\-0-9]+$)$', ProjectDetail.as_view(), name='project_detail'),
    url(r'^projects$', ProjectList.as_view(), name='project_list'),
    url(r'^interior/(?P<slug>[a-z\-0-9]+$)$', InteriorDetail.as_view(), name='interior_detail'),
    url(r'^interiors$', InteriorList.as_view(), name='interior_list'),
    url(r'^blog$', BlogList.as_view(), name='blog_list'),
    url(r'^blog/(?P<slug>[a-z\-0-9]+$)$', BlogDetail.as_view(), name='blog_detail'),
    url(r'^$', PageView.as_view(), kwargs={'slug': 'main'}, name='page_main'),
    url(r'^(?P<slug>[a-z\-0-9]+$)$', PageView.as_view(), name='page'),
)
