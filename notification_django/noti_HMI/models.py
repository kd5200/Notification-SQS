from django.db import models

class notification (models.Model):
    message = models.CharField(max_length=250)
    recipient = models.CharField(max_length=90)
    created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
