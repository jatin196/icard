from django.db import models

class IdInfo(models.Model):
    Name = models.CharField(max_length=45)
    DateOfBirth = models.DateField()
    Address = models.TextField()
    Job = models.CharField(max_length=45)

    def __str__(self):
        return self.Name
