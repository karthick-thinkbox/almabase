from django.db import models

class Inventory(models.Model):
    title = models.CharField(max_length=56, blank=True)
    platform = models.CharField(max_length=16, blank=True, null=True)
    score = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    genre = models.CharField(max_length=17, blank=True, null=True)
    editors_choice = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'

