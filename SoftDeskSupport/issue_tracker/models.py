from django.db import models

# Create your models here.


class Project(models.Model):
    TYPE_CHOICES = [
        ('back-end', 'Back-end'),
        ('front-end', 'Front-end'),
        ('iOS', 'iOS'),
        ('Android', 'Android'),
    ]


    name = models.CharField()

    description = models.CharField()

    project_type = models.CharField(choices=TYPE_CHOICES)

    #author = models.ForeignKey(User, on_delete=models.CASCADE)

class Issue(models.Model):
    name = models.CharField()

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    

class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)