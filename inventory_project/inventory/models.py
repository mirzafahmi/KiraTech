from django.db import models
from common.mixins import TimeMixin 

class Supplier(TimeMixin, models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

class Inventory(TimeMixin, models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    description = models.CharField(max_length=255)
    note = models.TextField()
    stock = models.PositiveIntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    availability = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Inventories"

    def __str__(self):
        return self.name