from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class CustomUserModel(AbstractUser):
    """
    Custom user model with email as username
    """
    def __str__(self):
        """
        String representation of user instance

        Returns:
            str: the username of the user
        """
        return self.username

class Task(models.Model):
    """
    Model representing a Task
    """

    LOW = 1
    MEDIUM = 2
    HIGH = 3

    PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High')
    )

    user = models.ForeignKey(
        CustomUserModel, 
        on_delete=models.CASCADE, 
        related_name='tasks',
        help_text='The user who created this task',
        default=None,
    )

    title = models.CharField(max_length=100, help_text='The title of the task')
    description = models.TextField(help_text='The description of the task')
    due_date = models.DateField(default=date.today, help_text='The due date of the task')
    completed = models.BooleanField(help_text='Whether the task is completed or not')
    priority_level = models.IntegerField(choices=PRIORITY_CHOICES, default=MEDIUM, help_text='The priority of the task')


    # Standard Django save() method used when you want to save an instance of a django model to a database
    # performs INSERT and UPDATE actions
    def save(self, *args, **kwargs):
        """
        Overrides the save method
        """
        if not self.user_id: 
            self.user = kwargs.pop('user', None)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of a user instance.
        
        Returns:
            the username of the user
        """
        return self.title
    
class Tag(models.Model):
    """
    Model Representing a tag attached to a task.
    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE, help_text='The task the tag is associated with')
    tag_name = models.CharField(max_length=100, help_text='The name of the tag')
    
    def __str__(self):
        """
        String representation of a Tag

        Returns:
            The name of a tag
        """
        return self.tag_name  
