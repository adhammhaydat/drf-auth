from django.urls import path
from .views import BookCreateView,BookDetailView

urlpatterns = [
    path('',BookCreateView.as_view(), name='list-view'),
    path('<int:pk>/',BookDetailView.as_view(), name='detail'),
]