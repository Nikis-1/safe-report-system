from django.urls import path
from .views import ReportCreateView

urlpatterns = [
    path('submit/', ReportCreateView.as_view(), name='submit-report'),
]
