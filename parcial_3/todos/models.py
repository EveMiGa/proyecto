from django.db import models


class Todo(models.Model):
    Nombre = models.CharField(max_length=100)
    Email = models.IntegerField()

    def __str__(self):
        return self.title
