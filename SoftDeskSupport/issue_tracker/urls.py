from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, IssueViewSet, CommentViewSet, ContributorViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'issues', IssueViewSet, basename='issue')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'contributors', ContributorViewSet, basename='contributor')

urlpatterns = [
     path('', include(router.urls)),
]