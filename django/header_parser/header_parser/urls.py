from django.urls import path
from mainapp.views import HeaderParserView

urlpatterns = [
    path('api/whoami', HeaderParserView.as_view())
]
