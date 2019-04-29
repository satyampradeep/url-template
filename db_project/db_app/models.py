from django.db import models

class Topic(models.Model):
    top_name=models.CharField(max_length=264,unique=True,default="",editable=False)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.PROTECT)
    name=models.CharField(max_length=264,unique=True,default="",editable=False)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.PROTECT)
    date=models.DateField(default="",editable=False)

    def __str__(self):
        return str(self.date)
