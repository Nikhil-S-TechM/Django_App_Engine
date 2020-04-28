from django.db import models

# Create your models here.
class Process(models.Model):
    pid = models.CharField(max_length=50)
    remark = models.CharField(max_length=255)

    def __str__(self):
        return self.pid + " - " + self.remark