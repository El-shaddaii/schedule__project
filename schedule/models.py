# models.py
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100, default='Unnamed Event')
    day = models.CharField(max_length=3)  # e.g., 'Mon', 'Tue'
    start_hour = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    nickname = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname  # Display nickname in admin
