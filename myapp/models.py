from django.db import models


class Snippet(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phno=models.IntegerField(max_length=100,default=0)
    body=models.TextField()

    def __str__(self):
        return self.name