from django.db import models

# Create your models here.
class Members(models.Model):
    Position_Choices = (
        ('Mem','Member'),
        ('CSe','Secretary'),
        ('CTr','Treasurer'),
        ('CVP','Vice President'),
        ('CPr','President'),
        ('FSe','Former-Secretary'),
        ('FTr','Former-Treasurer'),
        ('FVP','Former-Vice President'),
        ('FPr','Former-President'),
    )
    member_id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    position=models.CharField(max_length=3,choices=Position_Choices,default='Mem',)
    phone=models.IntegerField()
    email=models.CharField(max_length=100)
    image=models.CharField(max_length=50)


class Trips(models.Model):
    trip_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=255)
    restriction=models.CharField(max_length=255)
    deadline=models.DateField()
    regrister=models.CharField(max_length=255)


class Project(models.Model):
    project_id=models.AutoField(primary_key=True)
    image=models.CharField(max_length=50)
    date = models.DateField()
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=255)



