from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from .models import Project, Issue, Comment, Contributor
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer, ContributorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .permissions import IsContributorOrOwner

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsContributorOrOwner]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['author']
    ordering_fields = ['created_time']

    def get_queryset(self):
        project = self.request.data.get('project')
        if project is not None :
            return Project.objects.filter(id=project).select_related("author").prefetch_related("contributors")
        return Project.objects.filter(author = self.request.user).select_related("author").prefetch_related("contributors").order_by("-id")

class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsContributorOrOwner]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['author', 'project', 'priority', 'tag', 'status']
    ordering_fields = ['created_time']

    def get_queryset(self):
        project_id = self.request.data.get('project')
        issue_id = self.request.data.get('issue')

        project = get_object_or_404(Project, id=project_id)

        queryset = Issue.objects.filter(project=project)
        if issue_id:
            queryset = queryset.filter(id=issue_id)

        return queryset.select_related("author", "project").order_by("-id")

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsContributorOrOwner]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_time = ['author', 'title', 'project', 'priority', 'tag', 'status']
    ordering_fields = ['created_time']

    def get_queryset(self):
        issue_id = self.request.data.get('issue')
        comment_id = self.request.data.get('comment')
        issue = get_object_or_404(Issue, id=issue_id)
        queryset = Comment.objects.filter(issue=issue)
        if comment_id:
            queryset = queryset.filter(id=comment_id)
        return queryset.select_related("issue").order_by("-id")
        

class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all().select_related("user", "project").order_by("-id")
    serializer_class = ContributorSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated, IsContributorOrOwner]

