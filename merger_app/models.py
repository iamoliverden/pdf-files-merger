from django.db import models

# Create your models here.
from django.db import models

class Action(models.Model):
    folder_pickup = models.CharField(max_length=255)
    folder_send = models.CharField(max_length=255)
    date_action = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.folder_pickup} -> {self.folder_send} on {self.date_action}"
