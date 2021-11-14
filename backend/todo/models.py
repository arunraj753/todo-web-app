from django.db import models
from accounts.models import User

class ToDo(models.Model):

    task        = models.CharField(max_length=100)
    completed   = models.BooleanField(default=False)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
        return self.task
    class Meta:
        verbose_name_plural = 'ToDos'
