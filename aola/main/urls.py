from django.urls import path

from .api.views import FeedAPIView

urlpatterns = [
    path('feed/<user_id>/', FeedAPIView.as_view(), name='feed')
]
