import uuid
from django.db import models


class Task(models.Model):
    
    STATUS_CHOICES=[
        ('A', 'Active'),
        ('C', 'Completed')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    description = models.TextField()
    creation_date = models.DateTimeField()
    due_date = models.DateField()
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='A'
    )