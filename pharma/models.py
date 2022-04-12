from django.db import models

# Create your models here.

class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,)
    quantity = models.IntegerField()
    puchase_cost = models.FloatField()
    selling_cost = models.FloatField()


    class Meta:
        db_table = 'medicine'


class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table = 'bill'


