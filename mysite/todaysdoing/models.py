from django.db import models

class TODO(models.Model):
    doing_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class Result(models.Model):    
    achievement = models.BooleanField()
    pub_date = models.DateTimeField('date published')