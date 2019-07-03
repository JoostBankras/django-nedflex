from django.db import models

class Customer(models.Model):
    Name = models.TextField(default='None')
    Phone = models.TextField(default='None')
    Email = models.TextField(default='None')

    def __str__(self):
        return self.Name