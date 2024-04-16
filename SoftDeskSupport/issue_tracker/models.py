from django.db import models

from authentication.models import User

import uuid


# Create your models here.


class Project(models.Model):
    TYPE_CHOICES = [('Back-end', 'Back-end'), ('Front-end', 'Front-end'), ('iOS', 'iOS'), ('Android', 'Android')]
    title = models.CharField(max_length=100)
    description = models.TextField()

    project_type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    author = models.ForeignKey("authentication.User", on_delete=models.CASCADE, related_name='authored_projects')
    
    created_time = models.DateTimeField(auto_now_add=True)

    def get_contributors(self) :
        return self.contributors
class Issue(models.Model):
    PRIORITY_CHOICES = [('LOW', 'LOW'), ('MEDIUM', 'MEDIUM'), ('HIGH', 'HIGH')]
    
    TAG_CHOICES = [('BUG', 'BUG'), ('Feature', 'Feature'), ('TASK', 'TASK')]
    
    STATUS_CHOICES = [('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Finished', 'Finished')]

    author = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
    title = models.CharField(max_length=100)
    description = models.TextField()
    #assigned_to = models.ForeignKey("authentication.User", on_delete=models.CASCADE, related_name='assigned_issues')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    tag = models.CharField(max_length=10, choices=TAG_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do') #Remplace default par STATUS_CHOICES.TODO
    created_time = models.DateTimeField(auto_now_add=True)

    def get_contributors(self) :
        return self.project.get_contributors()

    

class Comment(models.Model):
    PRIORITY_CHOICES = [('LOW', 'LOW'), ('MEDIUM', 'MEDIUM'), ('HIGH', 'HIGH')]
    TAG_CHOICES = [('BUG', 'BUG'), ('Feature', 'Feature'), ('TASK', 'TASK')]
    STATUS_CHOICES = [('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Finished', 'Finished')]
    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comment')
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    tag = models.CharField(max_length=10, choices=TAG_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do')
    created_time = models.DateTimeField(auto_now_add=True)

    def get_contributors(self) :
        return self.issue.get_contributors()


class Contributor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="contributors")

    class Meta:
        unique_together = ('user', 'project')

    def get_contributors(self):
        return self.project.get_contributors()