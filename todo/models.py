from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoModel(models.Model):
    name  = models.CharField(max_length= 250)
    is_complated = models.BooleanField("Complated", default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todo_works")
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    # start_time = models.TimeField(blank=True, null=True)
    

    

    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "Works"

    def __str__(self):
        return self.name + "|" + self.user.username