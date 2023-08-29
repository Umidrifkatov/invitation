from django.db import models
import uuid


class Visitor(models.Model):
    name = models.CharField(max_length=100)
    seating_place = models.CharField(max_length=50, blank=True, null=True)
    unique_identifier = models.CharField(max_length=32, default=uuid.uuid4, editable=False, unique=True, null=True)



    



