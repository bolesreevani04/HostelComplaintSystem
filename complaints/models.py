from django.db import models

class Complaint(models.Model):
    category = models.CharField(max_length=255)
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category
