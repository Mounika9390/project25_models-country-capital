from django.db import models

# Create your models here.
class Country(models.Model):
    cid=models.PositiveIntegerField(primary_key=True)
    cname=models.CharField(max_length=100)

    def __str__(self):
        return self.cname
class Capital(models.Model):
    capital_id=models.PositiveIntegerField(primary_key=True)
    capital_name=models.CharField(max_length=100)
    cid=models.OneToOneField(Country,on_delete=models.CASCADE)
    def __str__(self):
        return self.capital_name