from django.db import models

class post(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=140)
    body = models.TextField()
    titleImg = models.CharField(null=True, max_length=50)
    views = models.IntegerField()
    beta = models.NullBooleanField(null=True)

    def __str__(self):
        return self.title