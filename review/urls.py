from django.urls import path, include
from rest_framework import routers

from .views import ReviewsViewSet, CommentsViewSet


v1_router = routers.DefaultRouter()
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewsViewSet,
    basename='ReviewsViewSet'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet,
    basename='CommentsViewSet'
)

urlpatterns = [
    path('v1/', include(v1_router.urls))
]
