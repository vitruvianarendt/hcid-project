from django.urls import path
from django.views.generic import TemplateView

from HW5App import admin

urlpatterns = [
    path('trala/', TemplateView.as_view(template_name='index.html'), name='index'),
]