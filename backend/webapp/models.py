from django.db import models

from webapp.views import add

# Create your models here.
class Sample(models.Model):
    name=models.CharField( max_length=50)
    add_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    