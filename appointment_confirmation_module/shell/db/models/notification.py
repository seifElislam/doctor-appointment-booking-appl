from datetime import datetime

from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    #TODO add user_id
    def __str__(self):
        return self.title