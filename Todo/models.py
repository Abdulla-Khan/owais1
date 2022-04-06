from operator import le
from django.db import models

# Create your models here.
class Todo(models.Model):
    
    username = models.CharField(max_length=20,null=True)
     

    def __str___(self):
        return self.username