from django.db import models

# Create your models here.

class Incident(models.Model):

    INCIDENT_TYPES = [
        ('fire', 'Fire'), 
        ('ems', 'EMS'), 
        ('traffic', 'Traffic'), 
        ('crime', 'Crime'),
        ('naturals', 'Naturals')
    ]

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    incident_type = models.CharField(max_length=10, choices=INCIDENT_TYPES)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} -> {self.incident_type}" 