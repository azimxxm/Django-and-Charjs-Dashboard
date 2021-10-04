from django.db import models

# Create your models here.
class CountryData(models.Model):
    coutry = models.CharField(max_length=100)
    popilation = models.IntegerField()

    class Meta:
        verbose_name = "Country Data"
        verbose_name_plural = "Country Data"

    def __str__(self):
        return f'{self.coutry} - {self.popilation}'