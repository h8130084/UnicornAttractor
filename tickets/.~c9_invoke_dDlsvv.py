from django.db import models
from django.contrib import auth

# Create your models here.
class Bug(models.Model):
    
    STATUS = [
        ('to do', 'To Do'),
        ('working on it', 'Working on it'),
        ('complete', 'Complete')
    ]
    
    TICKET_TYPE = [
        ('bug', 'Bug'),
        ('feature', 'Feature')
    ]
    
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    bug_or_feature = models.CharField(max_length=50, null=False, choices=TICKET_TYPE)
    upvotes = models.IntegerField(default=0, null=False) 
    pledge = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    userID = models.ForeignKey('auth.User', null=False, on_delete=models.SET_DEFAULT, default=1)
    time_stamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=False, default='to do', choices=STATUS)
    
    def __str__(self):
        return self.name
    
class Comments(models.Model):
    
    userID = models.ForeignKey('auth.User', null=False, on_delete=models.SET_DEFAULT, default=1)
    
    body = models.TextField()
    
    def __str__(self):
        return self.name