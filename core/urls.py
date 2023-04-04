from django.contrib import admin
from django.urls import path, include, re_path

from contact.views import EmailAPI

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('portfolio.urls')),
    re_path('contact', EmailAPI.as_view()),
]