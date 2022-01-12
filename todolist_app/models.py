from django.db import models
from django.contrib.auth.models import User #ders58 Relationship Between Task&User
   
    

class TaskList(models.Model):
    # ders59 yabancı anahtar ekleme  
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)#ders59
    task = models.CharField(max_length=256)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task + " - " + str(self.done)

