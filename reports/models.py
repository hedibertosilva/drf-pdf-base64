import uuid

from datetime import datetime
from django.db import models


class Reports(models.Model):

    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=datetime.now, null=False, blank=False) 
    title = models.CharField(max_length=255, null=False, blank=False)
    file = models.BinaryField(null=False, blank=False) 


    def __str__(self):
        return self.title