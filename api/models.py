from django.db import models
from unixtimestampfield.fields import UnixTimeStampField
# Create your models here.

class Resource(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()


    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    title = models.TextField()
    content = models.TextField()

    nd_date = UnixTimeStampField()
    s_date = UnixTimeStampField(auto_now_add=True)
    not_date = models.DateTimeField()

    resource_id = models.ForeignKey(Resource, on_delete=models.PROTECT)


    def __str__(self):
        return self.name
