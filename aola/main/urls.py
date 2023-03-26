from django.urls import path
from .views import FeedAPIView

urlpatterns = [
    path('feed/<user_id>/', FeedAPIView.as_view(), name='feed')
]