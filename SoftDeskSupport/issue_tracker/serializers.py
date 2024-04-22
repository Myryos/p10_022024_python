from dataclasses import fields
from rest_framework import serializers

from .models import Project, Issue, Comment, Contributor


class ContributorSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField()

    project = serializers.SerializerMethodField()
    
    def get_username(self,contributor):
        return contributor.user.username
    def get_project(self, contributor):
        return contributor.project.title
    class Meta:
        model = Contributor
        fields = ['username', 'project']
        read_only_fields = ['username', 'project']

class ProjectSerializer(serializers.ModelSerializer):
    contributors = ContributorSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'project_type', 'created_time', 'contributors']
        read_only_fields = ['created_time', 'contributors']
    def create(self, validated_data):
        request = self.context.get('request')
        if request:
            validated_data['author'] = request.user
        project = super().create(validated_data)
        Contributor.objects.create(user=request.user, project=project)
        return project
    

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['author','project','title', 'description', 'priority', 'tag', 'status', 'created_time']
        read_only_fields = ['created_time']

    def create(self, validated_data):
        request = self.context.get('request')
        if request:
            validated_data['author'] = request.user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'issue', 'title', 'description', 'priority', 'tag', 'status']
    def create(self, validated_data):
        request = self.context.get('request')
        if request:
            validated_data['author'] = request.user
        return super().create(validated_data)