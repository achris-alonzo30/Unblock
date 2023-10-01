from django.db import models


# Create your models here.
class Draft(models.Model):
    STATUS_CHOICES = (
        ('drafted', 'Drafted'),
        ('downloaded', 'Downloaded'),
    )

    title = models.CharField(max_length = 50, null = True, blank = True)
    content = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='drafted')

    def __str__(self):
        return self.title

