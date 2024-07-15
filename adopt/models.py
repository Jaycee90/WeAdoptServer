from django.db import models

# Create your models here.
class Available(models.Model):
    body = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    adopted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body
