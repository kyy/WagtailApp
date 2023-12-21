from django.db import models


class Datatable(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    url = models.CharField(max_length=100, default='')
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name
