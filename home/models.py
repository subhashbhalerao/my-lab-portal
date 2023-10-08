from django.db import models

# Create your models here.
class Exp_Lists(models.Model):
    subject = models.CharField(max_length=50)
    exp_no = models.IntegerField()
    sem = models.IntegerField()
    dt = models.DateField()
    file = models.FileField(upload_to="media/upload/")
    faculty = models.CharField(max_length=250)

    def __str__(self):
        return self.subject    
