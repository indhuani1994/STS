from django.db import models

# Create your models here.
class Placement_Model(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    student_id=models.CharField(max_length=100)
    coursename = models.CharField(max_length=100,null=True)
    photo=models.FileField(null=True)
    clogo=models.FileField()
    cname = models.CharField(max_length=100)
    crole=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100)
    package=models.DecimalField(max_digits = 5,
                         decimal_places = 2)
    status=models.CharField(max_length=100,default='Active', editable=False)
    class Meta:
            db_table = 'placement'
